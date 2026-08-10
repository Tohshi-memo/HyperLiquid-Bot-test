# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T00:07:26.687199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0749` n `12`; crypto_alt avg `0.1198` n `230`; crypto_major avg `0.1353` n `8`; equity avg `0.1523` n `112`; fx avg `0.03` n `6`; index avg `0.0131` n `25`; metal avg `0.0071` n `20`; unknown avg `0.0154` n `785`
- 1h: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.4484` n `230`; crypto_major avg `-0.3534` n `8`; equity avg `0.0596` n `112`; fx avg `0.0121` n `6`; index avg `0.0029` n `25`; metal avg `-0.0242` n `20`; unknown avg `-0.0263` n `785`
- 4h: commodity avg `0.2707` n `12`; crypto_alt avg `-1.0003` n `230`; crypto_major avg `-0.7953` n `8`; equity avg `-0.0776` n `112`; fx avg `0.0229` n `6`; index avg `-0.0225` n `25`; metal avg `-0.1655` n `20`; unknown avg `0.1589` n `785`
- 24h: commodity avg `0.4066` n `12`; crypto_alt avg `0.414` n `230`; crypto_major avg `-0.4347` n `8`; equity avg `0.152` n `112`; fx avg `0.0239` n `6`; index avg `0.0029` n `25`; metal avg `-0.0799` n `20`; unknown avg `-0.3918` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
