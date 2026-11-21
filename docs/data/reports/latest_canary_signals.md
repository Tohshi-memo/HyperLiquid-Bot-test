# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T15:52:27.577076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2679` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1407` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0` n `13`; crypto_alt avg `0.0401` n `239`; crypto_major avg `0.0472` n `8`; equity avg `0.0692` n `166`; fx avg `0.0031` n `6`; index avg `0.0062` n `27`; metal avg `0.0057` n `20`; unknown avg `-0.2984` n `1260`
- 1h: commodity avg `-0.0429` n `13`; crypto_alt avg `-0.1225` n `239`; crypto_major avg `-0.3841` n `8`; equity avg `0.0121` n `166`; fx avg `0.0082` n `6`; index avg `-0.0063` n `27`; metal avg `-0.0184` n `20`; unknown avg `201.1175` n `1250`
- 4h: commodity avg `0.0016` n `13`; crypto_alt avg `2.2462` n `239`; crypto_major avg `2.2695` n `8`; equity avg `0.7735` n `166`; fx avg `0.0205` n `6`; index avg `0.0838` n `27`; metal avg `0.1288` n `20`; unknown avg `202.4674` n `1244`
- 24h: commodity avg `0.5632` n `13`; crypto_alt avg `1.3667` n `239`; crypto_major avg `1.1039` n `8`; equity avg `-1.1869` n `166`; fx avg `-0.1048` n `6`; index avg `-0.2145` n `27`; metal avg `-0.0366` n `20`; unknown avg `43.9648` n `1141`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
