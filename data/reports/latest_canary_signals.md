# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T00:37:25.822711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `12`; crypto_alt avg `-0.0048` n `233`; crypto_major avg `-0.0668` n `8`; equity avg `0.1905` n `136`; fx avg `0.005` n `6`; index avg `0.0394` n `26`; metal avg `-0.0023` n `20`; unknown avg `2.8027` n `790`
- 1h: commodity avg `-0.1573` n `12`; crypto_alt avg `0.3496` n `233`; crypto_major avg `-0.0404` n `8`; equity avg `0.2126` n `136`; fx avg `-0.0251` n `6`; index avg `0.0451` n `26`; metal avg `0.0257` n `20`; unknown avg `2.2417` n `786`
- 4h: commodity avg `-0.1085` n `12`; crypto_alt avg `-0.7772` n `233`; crypto_major avg `-0.9043` n `8`; equity avg `-0.0585` n `136`; fx avg `-0.0033` n `6`; index avg `0.0245` n `26`; metal avg `0.0064` n `20`; unknown avg `0.602` n `732`
- 24h: commodity avg `1.0693` n `12`; crypto_alt avg `-2.0349` n `233`; crypto_major avg `-2.3465` n `8`; equity avg `-1.8742` n `136`; fx avg `0.1323` n `6`; index avg `-0.3021` n `26`; metal avg `-1.2382` n `20`; unknown avg `-0.2842` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
