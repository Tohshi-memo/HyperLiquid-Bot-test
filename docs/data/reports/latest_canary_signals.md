# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T10:22:23.997963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4815` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3791` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0242` n `13`; crypto_alt avg `-0.0641` n `239`; crypto_major avg `-0.0881` n `8`; equity avg `0.0605` n `166`; fx avg `0.0101` n `6`; index avg `0.0143` n `27`; metal avg `-0.0078` n `20`; unknown avg `0.2686` n `1261`
- 1h: commodity avg `0.0187` n `13`; crypto_alt avg `0.6314` n `239`; crypto_major avg `0.9092` n `8`; equity avg `0.2615` n `166`; fx avg `-0.0151` n `6`; index avg `0.0382` n `27`; metal avg `0.0434` n `20`; unknown avg `203.4951` n `1157`
- 4h: commodity avg `0.0299` n `13`; crypto_alt avg `1.8757` n `239`; crypto_major avg `2.5114` n `8`; equity avg `1.0942` n `166`; fx avg `-0.0198` n `6`; index avg `0.1263` n `27`; metal avg `0.1323` n `20`; unknown avg `132.9891` n `1137`
- 24h: commodity avg `-0.0606` n `13`; crypto_alt avg `3.1627` n `239`; crypto_major avg `4.2175` n `8`; equity avg `1.772` n `166`; fx avg `-0.0286` n `6`; index avg `0.2419` n `27`; metal avg `0.1316` n `20`; unknown avg `0.0644` n `1054`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
