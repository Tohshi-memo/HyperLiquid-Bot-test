# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T23:22:35.903381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `0.0064` n `230`; crypto_major avg `-0.0535` n `8`; equity avg `-0.0765` n `113`; fx avg `0.0003` n `6`; index avg `-0.0112` n `25`; metal avg `-0.0347` n `20`; unknown avg `-0.0269` n `785`
- 1h: commodity avg `-0.0238` n `12`; crypto_alt avg `-0.0924` n `230`; crypto_major avg `-0.0625` n `8`; equity avg `-0.2093` n `113`; fx avg `0.008` n `6`; index avg `-0.0186` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.1104` n `785`
- 4h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.458` n `230`; crypto_major avg `-0.2221` n `8`; equity avg `-0.7034` n `113`; fx avg `0.0101` n `6`; index avg `-0.0629` n `25`; metal avg `0.0051` n `20`; unknown avg `2.848` n `785`
- 24h: commodity avg `0.8183` n `12`; crypto_alt avg `-0.5775` n `230`; crypto_major avg `-0.5793` n `8`; equity avg `-1.863` n `113`; fx avg `0.2707` n `6`; index avg `-0.082` n `25`; metal avg `0.3192` n `20`; unknown avg `103.65` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
