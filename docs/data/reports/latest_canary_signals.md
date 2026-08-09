# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T18:37:28.186041+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `-0.0197` n `230`; crypto_major avg `-0.0261` n `8`; equity avg `0.0044` n `112`; fx avg `-0.0026` n `6`; index avg `0.0129` n `25`; metal avg `0.0032` n `20`; unknown avg `0.2695` n `785`
- 1h: commodity avg `0.0511` n `12`; crypto_alt avg `-0.0088` n `230`; crypto_major avg `-0.1408` n `8`; equity avg `0.0418` n `112`; fx avg `0.0063` n `6`; index avg `0.0303` n `25`; metal avg `0.006` n `20`; unknown avg `0.1979` n `785`
- 4h: commodity avg `0.0321` n `12`; crypto_alt avg `0.7274` n `230`; crypto_major avg `0.1243` n `8`; equity avg `0.114` n `112`; fx avg `0.0101` n `6`; index avg `0.0438` n `25`; metal avg `0.0291` n `20`; unknown avg `-0.039` n `785`
- 24h: commodity avg `0.0912` n `12`; crypto_alt avg `1.2349` n `230`; crypto_major avg `0.1604` n `8`; equity avg `0.2976` n `112`; fx avg `0.002` n `6`; index avg `0.0575` n `25`; metal avg `0.069` n `20`; unknown avg `0.3804` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
