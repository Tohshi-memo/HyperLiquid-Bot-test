# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T08:37:24.649472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `13`; crypto_alt avg `0.055` n `239`; crypto_major avg `0.0367` n `8`; equity avg `0.0025` n `163`; fx avg `0.0057` n `6`; index avg `0.0015` n `27`; metal avg `0.0149` n `20`; unknown avg `0.1326` n `1250`
- 1h: commodity avg `0.0344` n `13`; crypto_alt avg `0.1922` n `239`; crypto_major avg `0.2561` n `8`; equity avg `0.2607` n `163`; fx avg `-0.0286` n `6`; index avg `0.055` n `27`; metal avg `-0.1494` n `20`; unknown avg `0.1771` n `1226`
- 4h: commodity avg `-0.1588` n `13`; crypto_alt avg `0.5435` n `239`; crypto_major avg `0.4526` n `8`; equity avg `0.5949` n `163`; fx avg `-0.0776` n `6`; index avg `0.074` n `27`; metal avg `-0.3181` n `20`; unknown avg `0.66` n `1202`
- 24h: commodity avg `-0.1076` n `13`; crypto_alt avg `0.5977` n `239`; crypto_major avg `1.1982` n `8`; equity avg `0.9337` n `163`; fx avg `-0.1517` n `6`; index avg `0.0851` n `27`; metal avg `-1.0661` n `20`; unknown avg `5.6355` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
