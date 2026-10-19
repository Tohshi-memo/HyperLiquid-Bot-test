# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T02:37:26.854423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `0.0086` n `237`; crypto_major avg `0.0337` n `8`; equity avg `0.2839` n `151`; fx avg `-0.0096` n `6`; index avg `0.0269` n `26`; metal avg `-0.004` n `20`; unknown avg `0.0105` n `1194`
- 1h: commodity avg `-0.0231` n `13`; crypto_alt avg `0.0123` n `237`; crypto_major avg `0.0794` n `8`; equity avg `0.2975` n `151`; fx avg `-0.0491` n `6`; index avg `0.0385` n `26`; metal avg `0.0383` n `20`; unknown avg `0.1256` n `1192`
- 4h: commodity avg `-0.0989` n `13`; crypto_alt avg `1.547` n `237`; crypto_major avg `1.1064` n `8`; equity avg `1.7501` n `151`; fx avg `-0.0666` n `6`; index avg `0.2706` n `26`; metal avg `0.0715` n `20`; unknown avg `1.0383` n `1128`
- 24h: commodity avg `-0.4244` n `13`; crypto_alt avg `-0.0676` n `237`; crypto_major avg `0.6474` n `8`; equity avg `2.6042` n `151`; fx avg `-0.0663` n `6`; index avg `0.4826` n `26`; metal avg `0.2734` n `20`; unknown avg `3.0492` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2011`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1473`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1086`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0935`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0615`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0609`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
