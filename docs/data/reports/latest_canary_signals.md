# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T22:55:52.339253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `0.3061` n `228`; crypto_major avg `0.3859` n `8`; equity avg `0.0878` n `78`; fx avg `-0.0003` n `6`; index avg `0.0136` n `23`; metal avg `0.0616` n `18`; unknown avg `0.4011` n `702`
- 1h: commodity avg `-0.2675` n `12`; crypto_alt avg `-0.0483` n `228`; crypto_major avg `-0.0092` n `8`; equity avg `-0.1635` n `78`; fx avg `-0.0048` n `6`; index avg `-0.0464` n `23`; metal avg `0.0659` n `18`; unknown avg `0.0554` n `702`
- 4h: commodity avg `-0.1703` n `12`; crypto_alt avg `-1.1254` n `228`; crypto_major avg `-0.7883` n `8`; equity avg `-0.259` n `78`; fx avg `-0.0528` n `6`; index avg `-0.0682` n `23`; metal avg `-0.0091` n `18`; unknown avg `0.4009` n `694`
- 24h: commodity avg `0.1294` n `12`; crypto_alt avg `-0.3595` n `228`; crypto_major avg `-1.2811` n `8`; equity avg `-0.1124` n `78`; fx avg `-0.1238` n `6`; index avg `-0.0995` n `23`; metal avg `-0.1203` n `18`; unknown avg `0.4806` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
