# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T15:40:54.567647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `0.1185` n `229`; crypto_major avg `0.0993` n `8`; equity avg `-0.01` n `88`; fx avg `0.0087` n `6`; index avg `-0.0177` n `25`; metal avg `-0.0127` n `20`; unknown avg `0.036` n `747`
- 1h: commodity avg `-0.024` n `12`; crypto_alt avg `0.2574` n `229`; crypto_major avg `0.2557` n `8`; equity avg `0.0248` n `88`; fx avg `-0.0139` n `6`; index avg `-0.0229` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.1301` n `747`
- 4h: commodity avg `-0.0172` n `12`; crypto_alt avg `0.6039` n `229`; crypto_major avg `0.7947` n `8`; equity avg `-0.0237` n `88`; fx avg `-0.0828` n `6`; index avg `0.0302` n `25`; metal avg `0.0077` n `20`; unknown avg `0.2678` n `747`
- 24h: commodity avg `-0.0114` n `12`; crypto_alt avg `-1.3566` n `229`; crypto_major avg `-0.8328` n `8`; equity avg `0.2553` n `88`; fx avg `-0.0952` n `6`; index avg `0.0606` n `25`; metal avg `0.0672` n `20`; unknown avg `-0.5515` n `713`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
