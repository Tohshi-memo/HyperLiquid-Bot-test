# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T16:22:24.931003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1784` n `12`; crypto_alt avg `-0.2658` n `228`; crypto_major avg `-0.1592` n `8`; equity avg `-0.0061` n `69`; fx avg `-0.0183` n `6`; index avg `0.0018` n `23`; metal avg `0.0007` n `18`; unknown avg `-0.2592` n `419`
- 1h: commodity avg `0.1445` n `12`; crypto_alt avg `0.5639` n `228`; crypto_major avg `0.337` n `8`; equity avg `0.4579` n `69`; fx avg `-0.0086` n `6`; index avg `0.1127` n `23`; metal avg `-0.3434` n `18`; unknown avg `-0.0509` n `418`
- 4h: commodity avg `-0.3201` n `12`; crypto_alt avg `1.4016` n `228`; crypto_major avg `1.4484` n `8`; equity avg `0.7639` n `69`; fx avg `0.109` n `6`; index avg `-0.1106` n `23`; metal avg `0.4194` n `18`; unknown avg `0.4787` n `417`
- 24h: commodity avg `-0.3723` n `12`; crypto_alt avg `1.9545` n `228`; crypto_major avg `2.1173` n `8`; equity avg `1.9712` n `69`; fx avg `0.1834` n `6`; index avg `-0.0301` n `23`; metal avg `0.2061` n `18`; unknown avg `1.0588` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
