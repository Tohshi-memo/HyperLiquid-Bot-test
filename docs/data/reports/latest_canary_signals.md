# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T00:37:26.554507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.034` n `12`; crypto_alt avg `0.1488` n `233`; crypto_major avg `-0.0341` n `8`; equity avg `0.0173` n `136`; fx avg `0.0018` n `6`; index avg `0.0106` n `26`; metal avg `0.0041` n `20`; unknown avg `0.2095` n `830`
- 1h: commodity avg `-0.0307` n `12`; crypto_alt avg `0.5805` n `233`; crypto_major avg `0.0368` n `8`; equity avg `0.1041` n `136`; fx avg `-0.0067` n `6`; index avg `0.0306` n `26`; metal avg `0.0161` n `20`; unknown avg `-0.2463` n `828`
- 4h: commodity avg `-0.1212` n `12`; crypto_alt avg `-0.125` n `233`; crypto_major avg `-0.6031` n `8`; equity avg `0.0915` n `136`; fx avg `-0.0241` n `6`; index avg `0.0375` n `26`; metal avg `-0.0166` n `20`; unknown avg `2.9743` n `814`
- 24h: commodity avg `-0.6745` n `12`; crypto_alt avg `1.0247` n `233`; crypto_major avg `1.4395` n `8`; equity avg `0.7983` n `136`; fx avg `-0.1894` n `6`; index avg `0.3094` n `26`; metal avg `0.2611` n `20`; unknown avg `1.4201` n `702`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
