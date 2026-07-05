# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T13:37:28.829335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `-0.0737` n `229`; crypto_major avg `-0.105` n `8`; equity avg `0.0168` n `88`; fx avg `0.0041` n `6`; index avg `0.0079` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.0195` n `765`
- 1h: commodity avg `0.0062` n `12`; crypto_alt avg `-0.0342` n `229`; crypto_major avg `-0.1353` n `8`; equity avg `0.014` n `88`; fx avg `-0.0186` n `6`; index avg `0.0129` n `25`; metal avg `0.0137` n `20`; unknown avg `-0.0089` n `765`
- 4h: commodity avg `-0.0189` n `12`; crypto_alt avg `0.1172` n `229`; crypto_major avg `0.467` n `8`; equity avg `0.1293` n `88`; fx avg `-0.0348` n `6`; index avg `0.0265` n `25`; metal avg `0.0262` n `20`; unknown avg `-0.0442` n `765`
- 24h: commodity avg `-0.0126` n `12`; crypto_alt avg `-0.9099` n `229`; crypto_major avg `-0.4274` n `8`; equity avg `0.3625` n `88`; fx avg `-0.0209` n `6`; index avg `0.0621` n `25`; metal avg `0.0868` n `20`; unknown avg `-1.2101` n `731`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
