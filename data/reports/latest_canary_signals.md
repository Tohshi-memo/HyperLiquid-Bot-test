# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T21:07:23.965464+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `0.0061` n `231`; crypto_major avg `-0.0059` n `8`; equity avg `-0.0126` n `128`; fx avg `0.0` n `6`; index avg `-0.0004` n `26`; metal avg `0.0047` n `20`; unknown avg `3.0468` n `792`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `-0.1519` n `231`; crypto_major avg `-0.134` n `8`; equity avg `0.0286` n `128`; fx avg `-0.0004` n `6`; index avg `-0.0025` n `26`; metal avg `0.009` n `20`; unknown avg `7.7886` n `792`
- 4h: commodity avg `0.0015` n `12`; crypto_alt avg `-0.0769` n `231`; crypto_major avg `0.0248` n `8`; equity avg `0.1733` n `128`; fx avg `-0.0085` n `6`; index avg `0.0355` n `26`; metal avg `0.0259` n `20`; unknown avg `0.1248` n `792`
- 24h: commodity avg `-0.0215` n `12`; crypto_alt avg `0.7094` n `231`; crypto_major avg `1.142` n `8`; equity avg `0.379` n `128`; fx avg `-0.0125` n `6`; index avg `0.0793` n `26`; metal avg `0.1318` n `20`; unknown avg `0.2196` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2248`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
