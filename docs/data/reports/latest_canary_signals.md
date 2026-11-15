# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T12:07:29.327554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2584` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1401` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8494` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0031` n `13`; crypto_alt avg `-0.0078` n `239`; crypto_major avg `-0.2425` n `8`; equity avg `-0.0272` n `162`; fx avg `-0.0064` n `6`; index avg `-0.0055` n `27`; metal avg `0.0033` n `20`; unknown avg `-0.1851` n `1251`
- 1h: commodity avg `0.0003` n `13`; crypto_alt avg `0.1254` n `239`; crypto_major avg `-0.1652` n `8`; equity avg `-0.0042` n `162`; fx avg `-0.0175` n `6`; index avg `-0.0015` n `27`; metal avg `0.0028` n `20`; unknown avg `-0.2563` n `1255`
- 4h: commodity avg `-0.007` n `13`; crypto_alt avg `1.5798` n `239`; crypto_major avg `2.2514` n `8`; equity avg `0.402` n `162`; fx avg `-0.0379` n `6`; index avg `0.0393` n `27`; metal avg `0.1113` n `20`; unknown avg `0.1463` n `1255`
- 24h: commodity avg `0.0273` n `13`; crypto_alt avg `-3.9414` n `239`; crypto_major avg `-3.3124` n `8`; equity avg `-0.7507` n `162`; fx avg `0.0043` n `6`; index avg `-0.0612` n `27`; metal avg `-0.3417` n `20`; unknown avg `-0.3014` n `1134`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
