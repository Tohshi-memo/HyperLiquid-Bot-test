# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T23:52:29.636557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0234` n `12`; crypto_alt avg `0.1238` n `228`; crypto_major avg `-0.0173` n `8`; equity avg `0.0117` n `74`; fx avg `0.0219` n `6`; index avg `0.138` n `23`; metal avg `-0.2395` n `18`; unknown avg `-0.0314` n `550`
- 1h: commodity avg `0.001` n `12`; crypto_alt avg `0.5047` n `228`; crypto_major avg `0.2815` n `8`; equity avg `0.0149` n `74`; fx avg `0.038` n `6`; index avg `0.151` n `23`; metal avg `-0.3831` n `18`; unknown avg `-0.0678` n `550`
- 4h: commodity avg `0.7191` n `12`; crypto_alt avg `-0.4524` n `228`; crypto_major avg `-0.4352` n `8`; equity avg `-1.111` n `74`; fx avg `-0.0323` n `6`; index avg `-0.1123` n `23`; metal avg `-0.9311` n `18`; unknown avg `0.1917` n `550`
- 24h: commodity avg `1.5692` n `12`; crypto_alt avg `-2.0606` n `228`; crypto_major avg `-2.2964` n `8`; equity avg `-2.2809` n `74`; fx avg `-0.0466` n `6`; index avg `-1.4932` n `23`; metal avg `-2.4834` n `18`; unknown avg `-0.3602` n `537`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
