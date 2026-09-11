# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T10:52:27.942106+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0458` n `12`; crypto_alt avg `-0.114` n `233`; crypto_major avg `-0.0485` n `8`; equity avg `-0.052` n `136`; fx avg `-0.0025` n `6`; index avg `-0.0045` n `26`; metal avg `-0.0302` n `20`; unknown avg `0.0258` n `796`
- 1h: commodity avg `-0.1007` n `12`; crypto_alt avg `-0.4265` n `233`; crypto_major avg `-0.1561` n `8`; equity avg `-0.0663` n `136`; fx avg `-0.005` n `6`; index avg `0.0019` n `26`; metal avg `0.0013` n `20`; unknown avg `-0.1977` n `794`
- 4h: commodity avg `-0.4479` n `12`; crypto_alt avg `-0.9116` n `233`; crypto_major avg `-0.4846` n `8`; equity avg `0.1315` n `136`; fx avg `-0.1044` n `6`; index avg `0.049` n `26`; metal avg `-0.0334` n `20`; unknown avg `-0.4397` n `786`
- 24h: commodity avg `0.234` n `12`; crypto_alt avg `-1.7437` n `233`; crypto_major avg `-1.5608` n `8`; equity avg `-0.9087` n `136`; fx avg `-0.0833` n `6`; index avg `-0.1143` n `26`; metal avg `-0.4664` n `20`; unknown avg `1.0487` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
