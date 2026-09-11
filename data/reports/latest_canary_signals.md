# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T07:52:27.699421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.2382` n `233`; crypto_major avg `-0.1504` n `8`; equity avg `-0.0403` n `136`; fx avg `0.013` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0136` n `20`; unknown avg `-0.0049` n `796`
- 1h: commodity avg `-0.0403` n `12`; crypto_alt avg `-0.0597` n `233`; crypto_major avg `-0.1224` n `8`; equity avg `-0.0399` n `136`; fx avg `-0.0187` n `6`; index avg `-0.0201` n `26`; metal avg `-0.0547` n `20`; unknown avg `-0.0847` n `792`
- 4h: commodity avg `-0.44` n `12`; crypto_alt avg `0.5082` n `233`; crypto_major avg `0.6056` n `8`; equity avg `0.8525` n `136`; fx avg `0.0041` n `6`; index avg `0.1658` n `26`; metal avg `0.3529` n `20`; unknown avg `19.0506` n `762`
- 24h: commodity avg `0.7426` n `12`; crypto_alt avg `-1.1774` n `233`; crypto_major avg `-1.4706` n `8`; equity avg `-1.3742` n `136`; fx avg `0.0459` n `6`; index avg `-0.2351` n `26`; metal avg `-0.9974` n `20`; unknown avg `0.6025` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
