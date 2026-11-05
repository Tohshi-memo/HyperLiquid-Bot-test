# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T08:07:32.306507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0569` n `13`; crypto_alt avg `-0.1305` n `239`; crypto_major avg `0.0295` n `8`; equity avg `-0.1109` n `158`; fx avg `-0.022` n `6`; index avg `-0.0112` n `27`; metal avg `-0.0399` n `20`; unknown avg `1.3302` n `1243`
- 1h: commodity avg `0.2158` n `13`; crypto_alt avg `-0.4816` n `239`; crypto_major avg `-0.2691` n `8`; equity avg `-0.3109` n `158`; fx avg `-0.0492` n `6`; index avg `-0.0165` n `27`; metal avg `-0.0822` n `20`; unknown avg `1.6398` n `1241`
- 4h: commodity avg `0.2762` n `13`; crypto_alt avg `-0.5904` n `239`; crypto_major avg `-0.019` n `8`; equity avg `-0.2718` n `158`; fx avg `-0.0806` n `6`; index avg `-0.0392` n `27`; metal avg `-0.2163` n `20`; unknown avg `0.6213` n `1205`
- 24h: commodity avg `-1.6615` n `13`; crypto_alt avg `0.1307` n `239`; crypto_major avg `1.5743` n `8`; equity avg `-2.6815` n `158`; fx avg `-0.0021` n `6`; index avg `-0.1442` n `27`; metal avg `0.6996` n `20`; unknown avg `31.9857` n `1006`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2507`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
