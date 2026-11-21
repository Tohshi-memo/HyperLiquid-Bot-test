# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T12:52:26.512121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7321` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6711` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0225` n `13`; crypto_alt avg `-0.2304` n `239`; crypto_major avg `-0.2154` n `8`; equity avg `-0.0347` n `166`; fx avg `-0.0065` n `6`; index avg `0.0212` n `27`; metal avg `0.0059` n `20`; unknown avg `124.8455` n `1262`
- 1h: commodity avg `0.0324` n `13`; crypto_alt avg `0.4855` n `239`; crypto_major avg `0.6715` n `8`; equity avg `0.0594` n `166`; fx avg `-0.0077` n `6`; index avg `0.0284` n `27`; metal avg `0.0475` n `20`; unknown avg `162.3835` n `1248`
- 4h: commodity avg `0.0491` n `13`; crypto_alt avg `1.5012` n `239`; crypto_major avg `1.8111` n `8`; equity avg `0.14` n `166`; fx avg `-0.0003` n `6`; index avg `0.0333` n `27`; metal avg `0.079` n `20`; unknown avg `163.6074` n `1224`
- 24h: commodity avg `0.4482` n `13`; crypto_alt avg `-3.8873` n `239`; crypto_major avg `-4.1073` n `8`; equity avg `-3.6753` n `166`; fx avg `-0.1254` n `6`; index avg `-0.3911` n `27`; metal avg `-0.3232` n `20`; unknown avg `-0.1258` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
