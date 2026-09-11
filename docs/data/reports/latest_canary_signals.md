# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T05:22:26.362931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.0605` n `233`; crypto_major avg `-0.0472` n `8`; equity avg `0.0508` n `136`; fx avg `-0.0019` n `6`; index avg `0.0111` n `26`; metal avg `0.032` n `20`; unknown avg `36.8482` n `796`
- 1h: commodity avg `-0.0905` n `12`; crypto_alt avg `-0.0241` n `233`; crypto_major avg `0.1465` n `8`; equity avg `0.2484` n `136`; fx avg `0.0234` n `6`; index avg `0.0567` n `26`; metal avg `0.0955` n `20`; unknown avg `23.181` n `788`
- 4h: commodity avg `-0.1314` n `12`; crypto_alt avg `0.56` n `233`; crypto_major avg `0.4401` n `8`; equity avg `0.0002` n `136`; fx avg `-0.0445` n `6`; index avg `0.063` n `26`; metal avg `0.1141` n `20`; unknown avg `0.5084` n `780`
- 24h: commodity avg `0.9761` n `12`; crypto_alt avg `-1.6049` n `233`; crypto_major avg `-1.9428` n `8`; equity avg `-1.9412` n `136`; fx avg `0.0809` n `6`; index avg `-0.3156` n `26`; metal avg `-1.1999` n `20`; unknown avg `-0.3354` n `675`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
