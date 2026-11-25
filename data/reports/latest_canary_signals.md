# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T20:07:28.571617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.5218` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3537` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.9552` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0121` n `13`; crypto_alt avg `-0.1563` n `239`; crypto_major avg `-0.0397` n `8`; equity avg `-0.0498` n `168`; fx avg `0.0014` n `6`; index avg `-0.0012` n `27`; metal avg `0.1195` n `20`; unknown avg `0.6275` n `1251`
- 1h: commodity avg `-0.0405` n `13`; crypto_alt avg `0.1524` n `239`; crypto_major avg `0.2178` n `8`; equity avg `-0.2636` n `168`; fx avg `0.0053` n `6`; index avg `-0.0324` n `27`; metal avg `0.0681` n `20`; unknown avg `284.3724` n `1255`
- 4h: commodity avg `-0.0042` n `13`; crypto_alt avg `3.7146` n `239`; crypto_major avg `3.5176` n `8`; equity avg `5.4728` n `168`; fx avg `0.0719` n `6`; index avg `0.5506` n `27`; metal avg `1.1639` n `20`; unknown avg `322.3623` n `1256`
- 24h: commodity avg `0.3605` n `13`; crypto_alt avg `2.1651` n `239`; crypto_major avg `1.2717` n `8`; equity avg `-0.3839` n `168`; fx avg `0.0453` n `6`; index avg `-0.0495` n `27`; metal avg `0.1183` n `20`; unknown avg `1.4838` n `1087`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
