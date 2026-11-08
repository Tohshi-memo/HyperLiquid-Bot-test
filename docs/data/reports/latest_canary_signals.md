# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T20:37:24.372262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0239` n `13`; crypto_alt avg `0.0508` n `239`; crypto_major avg `-0.0312` n `8`; equity avg `-0.1201` n `158`; fx avg `0.0056` n `6`; index avg `-0.0262` n `27`; metal avg `-0.0083` n `20`; unknown avg `1.5142` n `1254`
- 1h: commodity avg `0.0225` n `13`; crypto_alt avg `-0.2249` n `239`; crypto_major avg `-0.1626` n `8`; equity avg `-0.4832` n `158`; fx avg `0.0015` n `6`; index avg `-0.0574` n `27`; metal avg `-0.0214` n `20`; unknown avg `12.2231` n `1230`
- 4h: commodity avg `-0.1148` n `13`; crypto_alt avg `-0.2554` n `239`; crypto_major avg `-0.2651` n `8`; equity avg `-0.0587` n `158`; fx avg `-0.0158` n `6`; index avg `-0.0176` n `27`; metal avg `0.0041` n `20`; unknown avg `1.6199` n `1178`
- 24h: commodity avg `-0.0897` n `13`; crypto_alt avg `-1.5704` n `239`; crypto_major avg `-0.2279` n `8`; equity avg `0.055` n `158`; fx avg `0.067` n `6`; index avg `-0.0375` n `27`; metal avg `-0.0318` n `20`; unknown avg `0.042` n `1024`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
