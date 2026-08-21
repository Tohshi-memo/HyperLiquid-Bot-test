# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T17:07:26.628339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0149` n `12`; crypto_alt avg `0.0975` n `230`; crypto_major avg `0.249` n `8`; equity avg `0.0596` n `121`; fx avg `0.0086` n `6`; index avg `0.0223` n `25`; metal avg `0.0129` n `20`; unknown avg `-0.176` n `793`
- 1h: commodity avg `0.0169` n `12`; crypto_alt avg `0.5763` n `230`; crypto_major avg `0.8483` n `8`; equity avg `0.0524` n `121`; fx avg `0.0002` n `6`; index avg `-0.004` n `25`; metal avg `0.0978` n `20`; unknown avg `0.3033` n `793`
- 4h: commodity avg `0.0406` n `12`; crypto_alt avg `0.8563` n `230`; crypto_major avg `0.8886` n `8`; equity avg `-0.4592` n `121`; fx avg `0.01` n `6`; index avg `-0.0497` n `25`; metal avg `0.0876` n `20`; unknown avg `0.283` n `793`
- 24h: commodity avg `0.3381` n `12`; crypto_alt avg `7.155` n `230`; crypto_major avg `3.9636` n `8`; equity avg `1.2832` n `121`; fx avg `-0.0924` n `6`; index avg `0.1049` n `25`; metal avg `0.6765` n `20`; unknown avg `1.1982` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2394`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1927`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
