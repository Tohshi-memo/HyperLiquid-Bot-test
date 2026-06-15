# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T20:52:37.884834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.38` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0945` n `12`; crypto_alt avg `-0.115` n `228`; crypto_major avg `-0.1944` n `8`; equity avg `-0.1068` n `77`; fx avg `-0.0016` n `6`; index avg `-0.0759` n `23`; metal avg `-0.0138` n `18`; unknown avg `0.0789` n `687`
- 1h: commodity avg `-0.1619` n `12`; crypto_alt avg `0.1053` n `228`; crypto_major avg `-0.1777` n `8`; equity avg `0.0061` n `77`; fx avg `-0.0167` n `6`; index avg `-0.0438` n `23`; metal avg `-0.1681` n `18`; unknown avg `-0.1287` n `687`
- 4h: commodity avg `0.361` n `12`; crypto_alt avg `-1.4051` n `228`; crypto_major avg `-1.1392` n `8`; equity avg `-0.0598` n `77`; fx avg `-0.0396` n `6`; index avg `-0.1397` n `23`; metal avg `-0.3863` n `18`; unknown avg `1.0843` n `687`
- 24h: commodity avg `-0.4116` n `12`; crypto_alt avg `4.3678` n `228`; crypto_major avg `6.1869` n `8`; equity avg `2.894` n `76`; fx avg `0.0363` n `6`; index avg `1.2103` n `23`; metal avg `1.8765` n `18`; unknown avg `5.7259` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
