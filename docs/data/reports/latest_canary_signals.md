# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T19:37:33.554246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `13`; crypto_alt avg `0.1122` n `239`; crypto_major avg `0.0912` n `8`; equity avg `-0.1256` n `162`; fx avg `-0.0112` n `6`; index avg `-0.0169` n `27`; metal avg `-0.0382` n `20`; unknown avg `-0.1943` n `1262`
- 1h: commodity avg `-0.0596` n `13`; crypto_alt avg `0.2515` n `239`; crypto_major avg `0.25` n `8`; equity avg `0.238` n `162`; fx avg `-0.0078` n `6`; index avg `0.0436` n `27`; metal avg `-0.0778` n `20`; unknown avg `5.3926` n `1260`
- 4h: commodity avg `-0.1644` n `13`; crypto_alt avg `0.9916` n `239`; crypto_major avg `1.177` n `8`; equity avg `1.5789` n `162`; fx avg `-0.0873` n `6`; index avg `0.1377` n `27`; metal avg `-0.1449` n `20`; unknown avg `-0.4856` n `1254`
- 24h: commodity avg `-0.3544` n `13`; crypto_alt avg `0.4469` n `239`; crypto_major avg `-1.0549` n `8`; equity avg `-2.2334` n `162`; fx avg `-0.0773` n `6`; index avg `-0.165` n `27`; metal avg `-0.2972` n `20`; unknown avg `1.8904` n `1089`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
