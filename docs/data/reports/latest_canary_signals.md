# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T09:52:32.916254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0529` n `13`; crypto_alt avg `0.0122` n `239`; crypto_major avg `0.0295` n `8`; equity avg `0.1421` n `158`; fx avg `-0.0121` n `6`; index avg `0.0176` n `27`; metal avg `-0.0272` n `20`; unknown avg `11.807` n `1257`
- 1h: commodity avg `0.1369` n `13`; crypto_alt avg `-0.1682` n `239`; crypto_major avg `-0.1176` n `8`; equity avg `0.3224` n `158`; fx avg `-0.0342` n `6`; index avg `0.0638` n `27`; metal avg `-0.0184` n `20`; unknown avg `13.355` n `1181`
- 4h: commodity avg `0.3126` n `13`; crypto_alt avg `0.6508` n `239`; crypto_major avg `0.4714` n `8`; equity avg `0.9335` n `158`; fx avg `-0.0634` n `6`; index avg `0.1334` n `27`; metal avg `0.1049` n `20`; unknown avg `13.4134` n `1141`
- 24h: commodity avg `-1.5441` n `13`; crypto_alt avg `0.9083` n `239`; crypto_major avg `1.7418` n `8`; equity avg `-2.8082` n `158`; fx avg `-0.0747` n `6`; index avg `-0.2271` n `27`; metal avg `0.5721` n `20`; unknown avg `0.471` n `1074`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2455`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1894`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
