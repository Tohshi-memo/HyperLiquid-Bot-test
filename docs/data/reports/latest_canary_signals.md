# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T21:22:31.541805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0712` n `230`; crypto_major avg `-0.1558` n `8`; equity avg `0.0599` n `102`; fx avg `0.0034` n `6`; index avg `-0.0028` n `25`; metal avg `0.0093` n `20`; unknown avg `-0.1489` n `774`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `0.0842` n `230`; crypto_major avg `-0.0415` n `8`; equity avg `0.153` n `102`; fx avg `-0.0122` n `6`; index avg `-0.0027` n `25`; metal avg `0.0088` n `20`; unknown avg `3.7441` n `774`
- 4h: commodity avg `-0.1369` n `12`; crypto_alt avg `-0.05` n `230`; crypto_major avg `-0.3619` n `8`; equity avg `1.0022` n `102`; fx avg `0.0064` n `6`; index avg `0.1776` n `25`; metal avg `0.0331` n `20`; unknown avg `98.2034` n `774`
- 24h: commodity avg `-0.9928` n `12`; crypto_alt avg `-0.8313` n `230`; crypto_major avg `-0.4219` n `8`; equity avg `-0.9533` n `102`; fx avg `-0.0418` n `6`; index avg `-0.3349` n `25`; metal avg `0.1768` n `20`; unknown avg `97.6511` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1934`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
