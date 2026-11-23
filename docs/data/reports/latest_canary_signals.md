# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T14:37:28.616664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `5.5013` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `5.223` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `4.6441` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `4.5294` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `0.2496` n `239`; crypto_major avg `0.1714` n `8`; equity avg `-0.3365` n `166`; fx avg `-0.0252` n `6`; index avg `-0.0334` n `27`; metal avg `-0.0058` n `20`; unknown avg `483.9614` n `1266`
- 1h: commodity avg `0.0323` n `13`; crypto_alt avg `4.246` n `239`; crypto_major avg `5.2553` n `8`; equity avg `5.5186` n `166`; fx avg `-0.0659` n `6`; index avg `0.5435` n `27`; metal avg `0.7259` n `20`; unknown avg `395.1685` n `1262`
- 4h: commodity avg `-0.219` n `13`; crypto_alt avg `4.147` n `239`; crypto_major avg `5.2823` n `8`; equity avg `5.1109` n `166`; fx avg `-0.1284` n `6`; index avg `0.4918` n `27`; metal avg `0.6382` n `20`; unknown avg `9.1305` n `1252`
- 24h: commodity avg `-0.9801` n `13`; crypto_alt avg `5.0088` n `239`; crypto_major avg `6.745` n `8`; equity avg `7.3496` n `166`; fx avg `0.0685` n `6`; index avg `0.5886` n `27`; metal avg `1.0229` n `20`; unknown avg `8.6973` n `1061`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
