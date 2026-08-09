# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T16:52:23.071364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `0.024` n `230`; crypto_major avg `0.0265` n `8`; equity avg `0.0052` n `112`; fx avg `-0.0012` n `6`; index avg `0.0033` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0605` n `785`
- 1h: commodity avg `-0.059` n `12`; crypto_alt avg `0.2122` n `230`; crypto_major avg `0.015` n `8`; equity avg `0.0367` n `112`; fx avg `0.0022` n `6`; index avg `0.0104` n `25`; metal avg `0.0041` n `20`; unknown avg `-0.0513` n `785`
- 4h: commodity avg `-0.0635` n `12`; crypto_alt avg `0.9001` n `230`; crypto_major avg `0.6847` n `8`; equity avg `0.116` n `112`; fx avg `0.0116` n `6`; index avg `0.0178` n `25`; metal avg `0.0427` n `20`; unknown avg `0.1105` n `785`
- 24h: commodity avg `0.0926` n `12`; crypto_alt avg `1.106` n `230`; crypto_major avg `0.1126` n `8`; equity avg `0.3036` n `112`; fx avg `0.0051` n `6`; index avg `0.0303` n `25`; metal avg `0.0603` n `20`; unknown avg `0.3897` n `752`

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
