# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T01:07:36.376233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.055` n `12`; crypto_alt avg `0.1145` n `228`; crypto_major avg `0.1492` n `8`; equity avg `0.0242` n `74`; fx avg `-0.0022` n `6`; index avg `0.0005` n `23`; metal avg `0.0004` n `18`; unknown avg `1.9712` n `645`
- 1h: commodity avg `-0.043` n `12`; crypto_alt avg `-0.0352` n `228`; crypto_major avg `0.1248` n `8`; equity avg `0.052` n `74`; fx avg `0.0015` n `6`; index avg `0.03` n `23`; metal avg `0.0194` n `18`; unknown avg `1.4988` n `645`
- 4h: commodity avg `-0.2668` n `12`; crypto_alt avg `0.0017` n `228`; crypto_major avg `0.4921` n `8`; equity avg `0.1075` n `74`; fx avg `-0.0404` n `6`; index avg `-0.0166` n `23`; metal avg `0.2625` n `18`; unknown avg `1.4572` n `644`
- 24h: commodity avg `-0.7861` n `12`; crypto_alt avg `1.5697` n `228`; crypto_major avg `1.4529` n `8`; equity avg `0.4399` n `74`; fx avg `0.0225` n `6`; index avg `0.4502` n `23`; metal avg `0.2275` n `18`; unknown avg `0.8299` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
