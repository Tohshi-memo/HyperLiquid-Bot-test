# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T03:22:29.394504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.0783` n `230`; crypto_major avg `0.0474` n `8`; equity avg `-0.0242` n `112`; fx avg `-0.0012` n `6`; index avg `0.0094` n `25`; metal avg `0.0674` n `20`; unknown avg `0.004` n `785`
- 1h: commodity avg `-0.0092` n `12`; crypto_alt avg `0.1791` n `230`; crypto_major avg `0.2243` n `8`; equity avg `0.053` n `112`; fx avg `-0.0048` n `6`; index avg `0.0147` n `25`; metal avg `-0.012` n `20`; unknown avg `-0.1087` n `785`
- 4h: commodity avg `0.018` n `12`; crypto_alt avg `0.2463` n `230`; crypto_major avg `0.2335` n `8`; equity avg `-0.3126` n `112`; fx avg `0.1093` n `6`; index avg `0.0344` n `25`; metal avg `-0.1204` n `20`; unknown avg `-0.0969` n `785`
- 24h: commodity avg `0.3868` n `12`; crypto_alt avg `0.8968` n `230`; crypto_major avg `0.1272` n `8`; equity avg `-0.2258` n `112`; fx avg `0.0957` n `6`; index avg `0.0286` n `25`; metal avg `-0.1748` n `20`; unknown avg `-0.2937` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
