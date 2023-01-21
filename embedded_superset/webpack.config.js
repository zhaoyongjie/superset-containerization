const webpack = require('webpack');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

const APP_DIR = path.join(__dirname, 'src');
const ASSETS_DIR = path.join(__dirname, 'assets');
const BUILD_DIR = path.join(__dirname, 'dist');

const plugins = [
  new CleanWebpackPlugin(['dist']),
  new webpack.DefinePlugin({
    'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV),
  }),
  new HtmlWebpackPlugin({
    template: path.join(ASSETS_DIR, 'index.html'),
    minify: { removeComments: true },
    alwaysWriteToDisk: true,
    favicon: './assets/favicon.png',
  }),
];

module.exports = (env, options) => {
  return {
    entry: {
      bundle: [path.join(APP_DIR, 'index.js')],
    },
    output: {
      publicPath: '/',
      path: BUILD_DIR,
      filename: '[name].js',
      chunkFilename: '[name].js',
    },
    resolve: {
      extensions: ['.js', '.jsx', ".ts", ".tsx"],
    },
    module: {
      rules: [
        {
          test: /\.js(x?)$/,
          exclude: /node_modules/,
          loader: 'babel-loader'
        },
        {
          test: /\.ts(x?)$/,
          exclude: /node_modules/,
          use: [
            {
              loader: "ts-loader"
            }
          ]
        },
        {
          test: /\.css$/,
          use: [
            'style-loader',
            'css-loader'
          ]
        },
        {
          test: /\.less$/,
          use: [
            'less-loader',
          ]
        },
      ],
    },
    plugins: plugins,
    devServer: {
      static: {
        directory: path.join(__dirname, '../assets'),
      },
      compress: true,
      port: process.env.devServerPort || 8020,
      proxy: {
        '/api': `http://localhost:${process.env.backendPort || 5000}/api`,
      },
    }
  }
};
