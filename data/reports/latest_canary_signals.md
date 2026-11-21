# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T13:22:27.079986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2025` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1332` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6799` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0043` n `13`; crypto_alt avg `-0.0859` n `239`; crypto_major avg `-0.157` n `8`; equity avg `0.065` n `166`; fx avg `0.0072` n `6`; index avg `0.0099` n `27`; metal avg `0.0102` n `20`; unknown avg `0.0014` n `1260`
- 1h: commodity avg `0.0121` n `13`; crypto_alt avg `0.6814` n `239`; crypto_major avg `0.8147` n `8`; equity avg `0.3018` n `166`; fx avg `-0.0025` n `6`; index avg `0.0512` n `27`; metal avg `0.0538` n `20`; unknown avg `248.3027` n `1258`
- 4h: commodity avg `0.0443` n `13`; crypto_alt avg `1.4536` n `239`; crypto_major avg `2.2468` n `8`; equity avg `0.5669` n `166`; fx avg `-0.0057` n `6`; index avg `0.0711` n `27`; metal avg `0.1136` n `20`; unknown avg `163.4053` n `1226`
- 24h: commodity avg `0.3685` n `13`; crypto_alt avg `-2.9664` n `239`; crypto_major avg `-3.0829` n `8`; equity avg `-3.2326` n `166`; fx avg `-0.1397` n `6`; index avg `-0.3408` n `27`; metal avg `-0.1812` n `20`; unknown avg `174.6404` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
