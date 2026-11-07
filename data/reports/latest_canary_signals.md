# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T17:37:23.735662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `13`; crypto_alt avg `0.0658` n `239`; crypto_major avg `0.0796` n `8`; equity avg `0.0693` n `158`; fx avg `-0.0006` n `6`; index avg `-0.007` n `27`; metal avg `0.0014` n `20`; unknown avg `0.1173` n `1246`
- 1h: commodity avg `0.0174` n `13`; crypto_alt avg `0.1756` n `239`; crypto_major avg `0.1047` n `8`; equity avg `0.1033` n `158`; fx avg `0.0152` n `6`; index avg `0.0109` n `27`; metal avg `0.005` n `20`; unknown avg `0.0371` n `1239`
- 4h: commodity avg `0.0571` n `13`; crypto_alt avg `-0.29` n `239`; crypto_major avg `-0.1861` n `8`; equity avg `-0.1293` n `158`; fx avg `-0.0397` n `6`; index avg `0.0159` n `27`; metal avg `-0.0231` n `20`; unknown avg `163.1554` n `1225`
- 24h: commodity avg `0.2088` n `13`; crypto_alt avg `-1.1358` n `239`; crypto_major avg `-0.2418` n `8`; equity avg `0.993` n `158`; fx avg `0.003` n `6`; index avg `0.1166` n `27`; metal avg `0.098` n `20`; unknown avg `-0.1739` n `1095`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
