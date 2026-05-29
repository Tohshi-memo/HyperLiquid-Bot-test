# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T17:22:20.609095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0194` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6176` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.558` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1551` n `12`; crypto_alt avg `0.3019` n `228`; crypto_major avg `0.2306` n `8`; equity avg `0.0094` n `69`; fx avg `-0.0091` n `6`; index avg `-0.018` n `23`; metal avg `-0.1773` n `18`; unknown avg `0.1956` n `419`
- 1h: commodity avg `-0.0824` n `12`; crypto_alt avg `0.5101` n `228`; crypto_major avg `0.6876` n `8`; equity avg `0.0404` n `69`; fx avg `0.003` n `6`; index avg `0.1067` n `23`; metal avg `-0.1294` n `18`; unknown avg `0.319` n `419`
- 4h: commodity avg `-0.5631` n `12`; crypto_alt avg `2.6411` n `228`; crypto_major avg `2.4563` n `8`; equity avg `0.8983` n `69`; fx avg `0.0624` n `6`; index avg `-0.0622` n `23`; metal avg `-0.1613` n `18`; unknown avg `0.8432` n `417`
- 24h: commodity avg `-0.5061` n `12`; crypto_alt avg `1.9476` n `228`; crypto_major avg `2.3399` n `8`; equity avg `2.1231` n `69`; fx avg `0.1983` n `6`; index avg `0.0459` n `23`; metal avg `0.1176` n `18`; unknown avg `1.3781` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1956`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
