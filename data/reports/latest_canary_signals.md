# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T16:49:52.737877+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `0.0227` n `230`; crypto_major avg `0.018` n `8`; equity avg `0.0028` n `112`; fx avg `-0.0012` n `6`; index avg `0.0016` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.0248` n `785`
- 1h: commodity avg `-0.0615` n `12`; crypto_alt avg `0.2109` n `230`; crypto_major avg `0.0065` n `8`; equity avg `0.0344` n `112`; fx avg `0.0022` n `6`; index avg `0.0087` n `25`; metal avg `0.0034` n `20`; unknown avg `-0.0158` n `785`
- 4h: commodity avg `-0.0661` n `12`; crypto_alt avg `0.8986` n `230`; crypto_major avg `0.6761` n `8`; equity avg `0.1136` n `112`; fx avg `0.0116` n `6`; index avg `0.0161` n `25`; metal avg `0.042` n `20`; unknown avg `0.1331` n `785`
- 24h: commodity avg `0.0901` n `12`; crypto_alt avg `1.1035` n `230`; crypto_major avg `0.1041` n `8`; equity avg `0.3013` n `112`; fx avg `0.0051` n `6`; index avg `0.0286` n `25`; metal avg `0.0595` n `20`; unknown avg `0.4193` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
