# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T10:22:23.071742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9925` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.925` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2723` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1199` n `13`; crypto_alt avg `0.0253` n `239`; crypto_major avg `0.123` n `8`; equity avg `0.0105` n `166`; fx avg `0.0253` n `6`; index avg `-0.0174` n `27`; metal avg `0.0269` n `20`; unknown avg `-0.0633` n `1258`
- 1h: commodity avg `0.1153` n `13`; crypto_alt avg `0.1696` n `239`; crypto_major avg `0.29` n `8`; equity avg `0.1679` n `166`; fx avg `0.0174` n `6`; index avg `0.0051` n `27`; metal avg `0.0475` n `20`; unknown avg `320.6218` n `1256`
- 4h: commodity avg `0.0831` n `13`; crypto_alt avg `2.0954` n `239`; crypto_major avg `3.0756` n `8`; equity avg `0.8033` n `166`; fx avg `-0.0131` n `6`; index avg `0.0619` n `27`; metal avg `0.1506` n `20`; unknown avg `402.3515` n `1232`
- 24h: commodity avg `0.931` n `13`; crypto_alt avg `-5.3089` n `239`; crypto_major avg `-6.0551` n `8`; equity avg `-4.4007` n `166`; fx avg `-0.0286` n `6`; index avg `-0.5047` n `27`; metal avg `-0.3594` n `20`; unknown avg `349.2168` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
