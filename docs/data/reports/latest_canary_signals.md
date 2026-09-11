# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T01:37:30.615702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0464` n `12`; crypto_alt avg `-0.0293` n `233`; crypto_major avg `-0.0869` n `8`; equity avg `0.0671` n `136`; fx avg `0.0081` n `6`; index avg `0.0001` n `26`; metal avg `0.0242` n `20`; unknown avg `0.2483` n `796`
- 1h: commodity avg `-0.1295` n `12`; crypto_alt avg `-0.0781` n `233`; crypto_major avg `0.0355` n `8`; equity avg `0.0074` n `136`; fx avg `-0.0025` n `6`; index avg `-0.011` n `26`; metal avg `0.0371` n `20`; unknown avg `-0.2132` n `794`
- 4h: commodity avg `-0.2905` n `12`; crypto_alt avg `-0.7296` n `233`; crypto_major avg `-0.7147` n `8`; equity avg `0.0496` n `136`; fx avg `0.0014` n `6`; index avg `0.0149` n `26`; metal avg `0.0059` n `20`; unknown avg `0.1017` n `750`
- 24h: commodity avg `0.9283` n `12`; crypto_alt avg `-1.4021` n `233`; crypto_major avg `-1.8183` n `8`; equity avg `-1.3725` n `136`; fx avg `0.1044` n `6`; index avg `-0.2216` n `26`; metal avg `-1.1941` n `20`; unknown avg `-0.8965` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
