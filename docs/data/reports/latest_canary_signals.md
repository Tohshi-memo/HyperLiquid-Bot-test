# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T05:22:30.118465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.2996` n `230`; crypto_major avg `-0.4808` n `8`; equity avg `-0.2993` n `98`; fx avg `-0.0209` n `6`; index avg `-0.042` n `25`; metal avg `-0.0388` n `20`; unknown avg `0.1348` n `771`
- 1h: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.4407` n `230`; crypto_major avg `-0.6751` n `8`; equity avg `-0.7371` n `98`; fx avg `-0.0298` n `6`; index avg `-0.1535` n `25`; metal avg `-0.0338` n `20`; unknown avg `-0.1679` n `771`
- 4h: commodity avg `-0.0695` n `11`; crypto_alt avg `-0.5901` n `230`; crypto_major avg `-0.8207` n `8`; equity avg `-1.5623` n `87`; fx avg `0.0147` n `5`; index avg `-0.2729` n `19`; metal avg `0.0125` n `16`; unknown avg `-0.5631` n `754`
- 24h: commodity avg `0.5597` n `12`; crypto_alt avg `-0.4799` n `230`; crypto_major avg `-0.763` n `8`; equity avg `1.7539` n `98`; fx avg `0.0546` n `6`; index avg `0.238` n `25`; metal avg `0.7331` n `20`; unknown avg `0.1628` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0984`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0638`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0585`, n `666`, weak_sample_signal
