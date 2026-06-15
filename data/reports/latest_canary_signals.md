# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T22:52:32.112944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.3` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.6058` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `-0.2585` n `228`; crypto_major avg `-0.1956` n `8`; equity avg `0.0118` n `77`; fx avg `0.0465` n `6`; index avg `0.0929` n `23`; metal avg `0.0386` n `18`; unknown avg `0.4926` n `687`
- 1h: commodity avg `0.0925` n `12`; crypto_alt avg `-0.9837` n `228`; crypto_major avg `-0.8193` n `8`; equity avg `-0.2007` n `77`; fx avg `0.0136` n `6`; index avg `-0.0205` n `23`; metal avg `-0.0239` n `18`; unknown avg `1.4926` n `687`
- 4h: commodity avg `0.1002` n `12`; crypto_alt avg `-1.7698` n `228`; crypto_major avg `-1.636` n `8`; equity avg `-0.2065` n `77`; fx avg `0.0215` n `6`; index avg `-0.0302` n `23`; metal avg `-0.2831` n `18`; unknown avg `0.9763` n `679`
- 24h: commodity avg `0.2133` n `12`; crypto_alt avg `0.9543` n `228`; crypto_major avg `2.6218` n `8`; equity avg `1.5729` n `76`; fx avg `-0.0445` n `6`; index avg `0.9858` n `23`; metal avg `0.2519` n `18`; unknown avg `3.0139` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
