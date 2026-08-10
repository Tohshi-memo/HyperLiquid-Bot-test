# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T04:22:31.021635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0251` n `12`; crypto_alt avg `0.1382` n `230`; crypto_major avg `0.058` n `8`; equity avg `0.0271` n `112`; fx avg `0.007` n `6`; index avg `0.0031` n `25`; metal avg `0.091` n `20`; unknown avg `-0.0462` n `785`
- 1h: commodity avg `0.0173` n `12`; crypto_alt avg `0.0334` n `230`; crypto_major avg `-0.1029` n `8`; equity avg `0.0655` n `112`; fx avg `-0.0044` n `6`; index avg `-0.0003` n `25`; metal avg `0.0888` n `20`; unknown avg `-0.1199` n `785`
- 4h: commodity avg `-0.0051` n `12`; crypto_alt avg `0.1004` n `230`; crypto_major avg `0.0073` n `8`; equity avg `-0.316` n `112`; fx avg `0.046` n `6`; index avg `0.0103` n `25`; metal avg `0.0201` n `20`; unknown avg `-0.28` n `785`
- 24h: commodity avg `0.3432` n `12`; crypto_alt avg `0.4951` n `230`; crypto_major avg `-0.0972` n `8`; equity avg `-0.1461` n `112`; fx avg `0.0968` n `6`; index avg `0.026` n `25`; metal avg `-0.0847` n `20`; unknown avg `-0.3117` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
