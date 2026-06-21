# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T01:37:25.235541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `0.2112` n `228`; crypto_major avg `0.0853` n `8`; equity avg `0.0203` n `78`; fx avg `0.0574` n `6`; index avg `-0.001` n `23`; metal avg `-0.0048` n `18`; unknown avg `-0.0524` n `701`
- 1h: commodity avg `-0.0141` n `12`; crypto_alt avg `0.3342` n `228`; crypto_major avg `0.0935` n `8`; equity avg `0.0389` n `78`; fx avg `-0.001` n `6`; index avg `0.0102` n `23`; metal avg `-0.0108` n `18`; unknown avg `0.4525` n `701`
- 4h: commodity avg `-0.0141` n `12`; crypto_alt avg `0.8285` n `228`; crypto_major avg `0.3749` n `8`; equity avg `0.1234` n `78`; fx avg `0.0089` n `6`; index avg `0.0137` n `23`; metal avg `-0.0201` n `18`; unknown avg `0.4291` n `701`
- 24h: commodity avg `0.3711` n `12`; crypto_alt avg `1.4409` n `228`; crypto_major avg `1.4326` n `8`; equity avg `0.4332` n `78`; fx avg `0.0467` n `6`; index avg `0.0237` n `23`; metal avg `-0.0513` n `18`; unknown avg `0.2477` n `557`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
