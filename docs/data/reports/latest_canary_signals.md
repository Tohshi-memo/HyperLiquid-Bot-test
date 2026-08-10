# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T02:37:31.428291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `-0.0286` n `230`; crypto_major avg `0.0517` n `8`; equity avg `0.0089` n `112`; fx avg `0.0003` n `6`; index avg `-0.0198` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.1489` n `785`
- 1h: commodity avg `-0.0506` n `12`; crypto_alt avg `-0.0449` n `230`; crypto_major avg `0.1373` n `8`; equity avg `-0.1207` n `112`; fx avg `0.0096` n `6`; index avg `-0.0285` n `25`; metal avg `0.127` n `20`; unknown avg `0.538` n `785`
- 4h: commodity avg `0.0499` n `12`; crypto_alt avg `-0.6214` n `230`; crypto_major avg `-0.3116` n `8`; equity avg `-0.2919` n `112`; fx avg `0.115` n `6`; index avg `0.0147` n `25`; metal avg `-0.067` n `20`; unknown avg `0.0989` n `785`
- 24h: commodity avg `0.4224` n `12`; crypto_alt avg `0.6008` n `230`; crypto_major avg `-0.1207` n `8`; equity avg `-0.3163` n `112`; fx avg `0.1091` n `6`; index avg `-0.0068` n `25`; metal avg `-0.1502` n `20`; unknown avg `-0.2564` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
