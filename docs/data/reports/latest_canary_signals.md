# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T23:07:33.172326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0` n `13`; crypto_alt avg `-0.3711` n `239`; crypto_major avg `-0.3473` n `8`; equity avg `-0.0193` n `160`; fx avg `0.009` n `6`; index avg `-0.0028` n `27`; metal avg `0.0129` n `20`; unknown avg `19.1051` n `1258`
- 1h: commodity avg `-0.0038` n `13`; crypto_alt avg `-0.4506` n `239`; crypto_major avg `-0.6603` n `8`; equity avg `-0.2284` n `160`; fx avg `0.0117` n `6`; index avg `-0.0136` n `27`; metal avg `0.0125` n `20`; unknown avg `20.0961` n `1256`
- 4h: commodity avg `0.1236` n `13`; crypto_alt avg `0.0554` n `239`; crypto_major avg `-0.0164` n `8`; equity avg `0.646` n `160`; fx avg `0.0045` n `6`; index avg `0.0465` n `27`; metal avg `0.0498` n `20`; unknown avg `40.0118` n `1226`
- 24h: commodity avg `0.1203` n `13`; crypto_alt avg `-1.2563` n `239`; crypto_major avg `-3.0853` n `8`; equity avg `-1.4116` n `160`; fx avg `-0.105` n `6`; index avg `-0.2035` n `27`; metal avg `-0.6308` n `20`; unknown avg `21.1349` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2578`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
