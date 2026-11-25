# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T19:07:28.445619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2307` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5072` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0677` n `13`; crypto_alt avg `0.2379` n `239`; crypto_major avg `0.1775` n `8`; equity avg `0.3609` n `168`; fx avg `-0.0082` n `6`; index avg `0.0058` n `27`; metal avg `0.0684` n `20`; unknown avg `0.3889` n `1257`
- 1h: commodity avg `-0.0718` n `13`; crypto_alt avg `0.5062` n `239`; crypto_major avg `0.4501` n `8`; equity avg `1.9217` n `168`; fx avg `0.0139` n `6`; index avg `0.178` n `27`; metal avg `0.2627` n `20`; unknown avg `200.5943` n `1263`
- 4h: commodity avg `0.0884` n `13`; crypto_alt avg `3.3005` n `239`; crypto_major avg `3.3191` n `8`; equity avg `4.2277` n `168`; fx avg `0.0903` n `6`; index avg `0.4139` n `27`; metal avg `0.8119` n `20`; unknown avg `191.099` n `1253`
- 24h: commodity avg `0.3005` n `13`; crypto_alt avg `1.2877` n `239`; crypto_major avg `0.4737` n `8`; equity avg `-0.6307` n `168`; fx avg `0.0146` n `6`; index avg `-0.0773` n `27`; metal avg `-0.0344` n `20`; unknown avg `205.6025` n `1083`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
