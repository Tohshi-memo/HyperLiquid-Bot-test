# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T00:07:29.630138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.267` n `12`; crypto_alt avg `0.3057` n `233`; crypto_major avg `0.1295` n `8`; equity avg `0.1182` n `136`; fx avg `-0.0399` n `6`; index avg `0.034` n `26`; metal avg `0.0649` n `20`; unknown avg `0.0935` n `790`
- 1h: commodity avg `-0.1418` n `12`; crypto_alt avg `0.0023` n `233`; crypto_major avg `0.0067` n `8`; equity avg `0.0311` n `136`; fx avg `-0.0283` n `6`; index avg `0.0011` n `26`; metal avg `0.0327` n `20`; unknown avg `-0.282` n `790`
- 4h: commodity avg `-0.0295` n `12`; crypto_alt avg `-0.745` n `233`; crypto_major avg `-0.7679` n `8`; equity avg `-0.094` n `136`; fx avg `-0.0135` n `6`; index avg `-0.015` n `26`; metal avg `0.0166` n `20`; unknown avg `-0.2915` n `732`
- 24h: commodity avg `0.9969` n `12`; crypto_alt avg `-2.5319` n `233`; crypto_major avg `-2.4375` n `8`; equity avg `-2.22` n `136`; fx avg `0.1033` n `6`; index avg `-0.3994` n `26`; metal avg `-1.2181` n `20`; unknown avg `-0.9623` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
