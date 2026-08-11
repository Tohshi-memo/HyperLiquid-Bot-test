# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T05:52:25.404357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0838` n `12`; crypto_alt avg `-0.0239` n `230`; crypto_major avg `-0.0288` n `8`; equity avg `-0.0649` n `113`; fx avg `-0.0018` n `6`; index avg `-0.0203` n `25`; metal avg `-0.0168` n `20`; unknown avg `-0.0441` n `785`
- 1h: commodity avg `0.0888` n `12`; crypto_alt avg `-0.0444` n `230`; crypto_major avg `-0.0656` n `8`; equity avg `-0.2491` n `113`; fx avg `-0.003` n `6`; index avg `-0.0529` n `25`; metal avg `-0.2402` n `20`; unknown avg `-0.3941` n `785`
- 4h: commodity avg `0.0317` n `12`; crypto_alt avg `-0.3298` n `230`; crypto_major avg `-0.1018` n `8`; equity avg `-0.0714` n `113`; fx avg `-0.0099` n `6`; index avg `-0.0114` n `25`; metal avg `-0.4779` n `20`; unknown avg `-0.3203` n `785`
- 24h: commodity avg `1.0485` n `12`; crypto_alt avg `-0.7952` n `230`; crypto_major avg `-0.7106` n `8`; equity avg `-1.007` n `113`; fx avg `0.0771` n `6`; index avg `0.017` n `25`; metal avg `-0.0061` n `20`; unknown avg `103.932` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
