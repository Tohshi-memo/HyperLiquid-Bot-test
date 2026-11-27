# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T02:52:24.596678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `13`; crypto_alt avg `-0.0897` n `239`; crypto_major avg `-0.2772` n `8`; equity avg `0.1787` n `168`; fx avg `0.0113` n `6`; index avg `0.0167` n `27`; metal avg `-0.0103` n `20`; unknown avg `1.1447` n `1263`
- 1h: commodity avg `0.0558` n `13`; crypto_alt avg `1.2597` n `239`; crypto_major avg `1.4311` n `8`; equity avg `1.5026` n `168`; fx avg `0.0091` n `6`; index avg `0.1251` n `27`; metal avg `0.5799` n `20`; unknown avg `0.1609` n `1253`
- 4h: commodity avg `0.1509` n `13`; crypto_alt avg `1.3081` n `239`; crypto_major avg `1.5699` n `8`; equity avg `2.2767` n `168`; fx avg `-0.0085` n `6`; index avg `0.2344` n `27`; metal avg `0.8911` n `20`; unknown avg `11.4082` n `1217`
- 24h: commodity avg `0.3048` n `13`; crypto_alt avg `1.5814` n `239`; crypto_major avg `1.4773` n `8`; equity avg `2.1271` n `168`; fx avg `0.038` n `6`; index avg `0.2109` n `27`; metal avg `0.6367` n `20`; unknown avg `181.7622` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
