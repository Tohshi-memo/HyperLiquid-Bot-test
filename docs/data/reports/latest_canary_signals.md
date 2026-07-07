# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T23:37:37.112333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `-0.1342` n `229`; crypto_major avg `-0.1922` n `8`; equity avg `-0.0391` n `91`; fx avg `0.01` n `6`; index avg `0.0073` n `25`; metal avg `-0.0186` n `20`; unknown avg `0.0405` n `763`
- 1h: commodity avg `0.0114` n `12`; crypto_alt avg `-0.0424` n `229`; crypto_major avg `-0.0759` n `8`; equity avg `-0.1878` n `91`; fx avg `0.047` n `6`; index avg `0.0032` n `25`; metal avg `0.0187` n `20`; unknown avg `-0.0885` n `763`
- 4h: commodity avg `0.1003` n `12`; crypto_alt avg `-0.6182` n `229`; crypto_major avg `-0.5301` n `8`; equity avg `-0.2223` n `91`; fx avg `0.0288` n `6`; index avg `0.0078` n `25`; metal avg `-0.1104` n `20`; unknown avg `0.0575` n `763`
- 24h: commodity avg `0.9351` n `12`; crypto_alt avg `-2.6859` n `229`; crypto_major avg `-1.6877` n `8`; equity avg `-3.293` n `91`; fx avg `-0.2404` n `6`; index avg `-0.5823` n `25`; metal avg `-0.641` n `20`; unknown avg `-0.0397` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
