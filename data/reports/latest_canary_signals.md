# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T02:22:16.791540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `12`; crypto_alt avg `-0.0956` n `228`; crypto_major avg `-0.1329` n `8`; equity avg `-0.2022` n `67`; fx avg `-0.0079` n `6`; index avg `-0.0831` n `23`; metal avg `-0.0095` n `18`; unknown avg `-0.103` n `419`
- 1h: commodity avg `-0.0514` n `12`; crypto_alt avg `0.0269` n `228`; crypto_major avg `-0.2703` n `8`; equity avg `-0.3656` n `67`; fx avg `-0.0133` n `6`; index avg `-0.0913` n `23`; metal avg `-0.5292` n `18`; unknown avg `-0.43` n `419`
- 4h: commodity avg `0.2259` n `12`; crypto_alt avg `-0.7474` n `228`; crypto_major avg `-0.878` n `8`; equity avg `-0.5687` n `67`; fx avg `-0.006` n `6`; index avg `-0.2456` n `23`; metal avg `-1.2492` n `18`; unknown avg `-0.3718` n `419`
- 24h: commodity avg `-0.6387` n `12`; crypto_alt avg `-2.0789` n `228`; crypto_major avg `-1.7973` n `8`; equity avg `-0.9776` n `67`; fx avg `-0.0678` n `6`; index avg `-0.8648` n `23`; metal avg `-2.2064` n `18`; unknown avg `-1.0842` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
