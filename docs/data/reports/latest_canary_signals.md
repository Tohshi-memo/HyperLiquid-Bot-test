# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T02:52:29.756835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0369` n `12`; crypto_alt avg `-0.1813` n `229`; crypto_major avg `-0.23` n `8`; equity avg `-0.1041` n `91`; fx avg `-0.0148` n `6`; index avg `-0.0217` n `25`; metal avg `-0.1448` n `20`; unknown avg `1.1513` n `763`
- 1h: commodity avg `-0.0101` n `12`; crypto_alt avg `-0.7037` n `229`; crypto_major avg `-0.8707` n `8`; equity avg `-0.5043` n `91`; fx avg `-0.0007` n `6`; index avg `-0.1409` n `25`; metal avg `-0.1363` n `20`; unknown avg `1.6008` n `763`
- 4h: commodity avg `0.0458` n `12`; crypto_alt avg `-1.2457` n `229`; crypto_major avg `-1.3196` n `8`; equity avg `-1.2237` n `91`; fx avg `-0.0726` n `6`; index avg `-0.3448` n `25`; metal avg `-0.2925` n `20`; unknown avg `1.9804` n `761`
- 24h: commodity avg `0.3161` n `12`; crypto_alt avg `-0.2396` n `229`; crypto_major avg `-0.9121` n `8`; equity avg `-0.6042` n `90`; fx avg `0.0075` n `6`; index avg `-0.1184` n `25`; metal avg `-0.3229` n `20`; unknown avg `-0.1845` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
