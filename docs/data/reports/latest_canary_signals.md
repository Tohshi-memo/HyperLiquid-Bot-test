# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T14:52:31.827192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2168` n `13`; crypto_alt avg `0.1291` n `239`; crypto_major avg `-0.228` n `8`; equity avg `0.2665` n `160`; fx avg `0.009` n `6`; index avg `0.0186` n `27`; metal avg `-0.0806` n `20`; unknown avg `0.2036` n `1264`
- 1h: commodity avg `0.2454` n `13`; crypto_alt avg `0.6349` n `239`; crypto_major avg `-0.1768` n `8`; equity avg `1.0188` n `160`; fx avg `0.012` n `6`; index avg `0.0652` n `27`; metal avg `-0.2015` n `20`; unknown avg `1.2441` n `1258`
- 4h: commodity avg `-0.0549` n `13`; crypto_alt avg `0.6446` n `239`; crypto_major avg `-0.6692` n `8`; equity avg `-0.4418` n `160`; fx avg `-0.0058` n `6`; index avg `-0.0316` n `27`; metal avg `-0.2955` n `20`; unknown avg `19.7861` n `1250`
- 24h: commodity avg `-0.5426` n `13`; crypto_alt avg `-0.4355` n `239`; crypto_major avg `-2.202` n `8`; equity avg `0.3066` n `160`; fx avg `-0.0226` n `6`; index avg `0.0507` n `27`; metal avg `-0.4847` n `20`; unknown avg `0.4685` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2181`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
