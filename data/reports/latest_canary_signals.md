# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T12:37:27.642286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0982` n `13`; crypto_alt avg `0.2227` n `239`; crypto_major avg `0.1945` n `8`; equity avg `0.0452` n `158`; fx avg `0.0205` n `6`; index avg `0.004` n `27`; metal avg `0.0106` n `20`; unknown avg `0.4016` n `1263`
- 1h: commodity avg `0.1522` n `13`; crypto_alt avg `0.7434` n `239`; crypto_major avg `0.4003` n `8`; equity avg `0.115` n `158`; fx avg `0.0182` n `6`; index avg `-0.003` n `27`; metal avg `-0.0091` n `20`; unknown avg `19.258` n `1251`
- 4h: commodity avg `-0.1516` n `13`; crypto_alt avg `2.1021` n `239`; crypto_major avg `0.6562` n `8`; equity avg `0.8107` n `158`; fx avg `-0.0427` n `6`; index avg `0.0942` n `27`; metal avg `0.0906` n `20`; unknown avg `155.5782` n `1241`
- 24h: commodity avg `-0.4385` n `13`; crypto_alt avg `-0.4065` n `239`; crypto_major avg `-2.9934` n `8`; equity avg `-0.1179` n `158`; fx avg `-0.1291` n `6`; index avg `0.0107` n `27`; metal avg `0.3411` n `20`; unknown avg `0.5808` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
