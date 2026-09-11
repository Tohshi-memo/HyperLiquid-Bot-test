# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T09:22:27.563031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.1502` n `233`; crypto_major avg `-0.1215` n `8`; equity avg `-0.1477` n `136`; fx avg `0.0052` n `6`; index avg `-0.0229` n `26`; metal avg `-0.0402` n `20`; unknown avg `-0.0246` n `796`
- 1h: commodity avg `-0.153` n `12`; crypto_alt avg `-0.1235` n `233`; crypto_major avg `-0.0026` n `8`; equity avg `0.264` n `136`; fx avg `-0.0572` n `6`; index avg `0.0426` n `26`; metal avg `0.0029` n `20`; unknown avg `-0.1549` n `788`
- 4h: commodity avg `-0.3877` n `12`; crypto_alt avg `-0.184` n `233`; crypto_major avg `0.1502` n `8`; equity avg `0.7196` n `136`; fx avg `-0.0578` n `6`; index avg `0.1336` n `26`; metal avg `0.1225` n `20`; unknown avg `0.8639` n `762`
- 24h: commodity avg `0.4306` n `12`; crypto_alt avg `-1.2906` n `233`; crypto_major avg `-1.4182` n `8`; equity avg `-0.9165` n `136`; fx avg `-0.0428` n `6`; index avg `-0.1259` n `26`; metal avg `-0.8416` n `20`; unknown avg `1.4359` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
