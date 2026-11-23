# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T15:22:29.812948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `5.0497` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.8853` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.2249` n `13`; crypto_alt avg `0.0884` n `239`; crypto_major avg `0.2943` n `8`; equity avg `0.6616` n `166`; fx avg `-0.0156` n `6`; index avg `0.0666` n `27`; metal avg `0.0131` n `20`; unknown avg `3.1703` n `1264`
- 1h: commodity avg `-0.594` n `13`; crypto_alt avg `-0.4535` n `239`; crypto_major avg `-0.5877` n `8`; equity avg `-0.1134` n `166`; fx avg `-0.0779` n `6`; index avg `0.0744` n `27`; metal avg `-0.0444` n `20`; unknown avg `1.1332` n `1262`
- 4h: commodity avg `-0.6252` n `13`; crypto_alt avg `3.3635` n `239`; crypto_major avg `4.4245` n `8`; equity avg `5.393` n `166`; fx avg `-0.1736` n `6`; index avg `0.6024` n `27`; metal avg `0.5392` n `20`; unknown avg `10.1889` n `1254`
- 24h: commodity avg `-1.5363` n `13`; crypto_alt avg `4.3014` n `239`; crypto_major avg `5.5834` n `8`; equity avg `7.505` n `166`; fx avg `0.0073` n `6`; index avg `0.7003` n `27`; metal avg `0.9494` n `20`; unknown avg `10.1061` n `1059`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
