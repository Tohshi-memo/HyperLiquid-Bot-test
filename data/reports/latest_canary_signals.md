# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T03:37:26.474602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0943` n `13`; crypto_alt avg `-0.0568` n `237`; crypto_major avg `0.0119` n `8`; equity avg `0.0032` n `151`; fx avg `0.0086` n `6`; index avg `-0.0001` n `26`; metal avg `0.0153` n `20`; unknown avg `2.6761` n `1194`
- 1h: commodity avg `-0.0713` n `13`; crypto_alt avg `-0.0761` n `237`; crypto_major avg `0.1508` n `8`; equity avg `0.2924` n `151`; fx avg `0.0528` n `6`; index avg `0.0583` n `26`; metal avg `0.0714` n `20`; unknown avg `1.1427` n `1192`
- 4h: commodity avg `-0.1198` n `13`; crypto_alt avg `0.5866` n `237`; crypto_major avg `0.6126` n `8`; equity avg `1.7765` n `151`; fx avg `0.0032` n `6`; index avg `0.3209` n `26`; metal avg `0.1404` n `20`; unknown avg `2.2487` n `1128`
- 24h: commodity avg `-0.5075` n `13`; crypto_alt avg `-0.3741` n `237`; crypto_major avg `0.5758` n `8`; equity avg `2.8493` n `151`; fx avg `0.0009` n `6`; index avg `0.5339` n `26`; metal avg `0.3285` n `20`; unknown avg `5.8843` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2003`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1466`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1121`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0879`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0655`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0654`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
