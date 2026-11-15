# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T09:22:23.354551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.1469` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.0385` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.6927` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.005` n `13`; crypto_alt avg `0.1615` n `239`; crypto_major avg `0.1939` n `8`; equity avg `0.0156` n `162`; fx avg `-0.0071` n `6`; index avg `-0.0079` n `27`; metal avg `0.0022` n `20`; unknown avg `0.2721` n `1261`
- 1h: commodity avg `-0.0026` n `13`; crypto_alt avg `1.6729` n `239`; crypto_major avg `2.1443` n `8`; equity avg `0.4516` n `162`; fx avg `-0.013` n `6`; index avg `0.044` n `27`; metal avg `0.1058` n `20`; unknown avg `1.229` n `1261`
- 4h: commodity avg `-0.028` n `13`; crypto_alt avg `0.3783` n `239`; crypto_major avg `0.8031` n `8`; equity avg `0.2031` n `162`; fx avg `-0.0264` n `6`; index avg `0.025` n `27`; metal avg `0.147` n `20`; unknown avg `1.185` n `1227`
- 24h: commodity avg `0.0198` n `13`; crypto_alt avg `-3.9886` n `239`; crypto_major avg `-2.7913` n `8`; equity avg `-0.5998` n `162`; fx avg `0.0284` n `6`; index avg `-0.0482` n `27`; metal avg `-0.3277` n `20`; unknown avg `45.6774` n `1110`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
