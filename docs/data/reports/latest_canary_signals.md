# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T13:07:23.626048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3147` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2571` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8869` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0039` n `13`; crypto_alt avg `0.5424` n `239`; crypto_major avg `0.6721` n `8`; equity avg `0.1805` n `166`; fx avg `0.0044` n `6`; index avg `0.012` n `27`; metal avg `0.0208` n `20`; unknown avg `0.7421` n `1252`
- 1h: commodity avg `0.0327` n `13`; crypto_alt avg `1.0958` n `239`; crypto_major avg `1.3268` n `8`; equity avg `0.3043` n `166`; fx avg `-0.0055` n `6`; index avg `0.0459` n `27`; metal avg `0.0725` n `20`; unknown avg `159.5096` n `1256`
- 4h: commodity avg `0.036` n `13`; crypto_alt avg `1.6287` n `239`; crypto_major avg `2.3507` n `8`; equity avg `0.4638` n `166`; fx avg `0.0088` n `6`; index avg `0.0635` n `27`; metal avg `0.0936` n `20`; unknown avg `0.3926` n `1220`
- 24h: commodity avg `0.5797` n `13`; crypto_alt avg `-3.1417` n `239`; crypto_major avg `-3.2744` n `8`; equity avg `-3.471` n `166`; fx avg `-0.1323` n `6`; index avg `-0.3683` n `27`; metal avg `-0.3099` n `20`; unknown avg `-0.2655` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
