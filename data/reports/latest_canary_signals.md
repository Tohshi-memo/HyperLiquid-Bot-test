# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T16:52:42.168301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.5576` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.0653` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.7722` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.4012` n `13`; crypto_alt avg `0.1769` n `239`; crypto_major avg `0.0853` n `8`; equity avg `0.703` n `158`; fx avg `-0.0247` n `6`; index avg `0.1144` n `27`; metal avg `0.0555` n `20`; unknown avg `12.8357` n `1264`
- 1h: commodity avg `-1.1766` n `13`; crypto_alt avg `-0.0898` n `239`; crypto_major avg `0.1684` n `8`; equity avg `0.3488` n `158`; fx avg `-0.031` n `6`; index avg `0.0927` n `27`; metal avg `0.1069` n `20`; unknown avg `0.4495` n `1252`
- 4h: commodity avg `-1.6117` n `13`; crypto_alt avg `2.1277` n `239`; crypto_major avg `2.9459` n `8`; equity avg `-0.1194` n `158`; fx avg `-0.0654` n `6`; index avg `0.1453` n `27`; metal avg `0.1737` n `20`; unknown avg `21.055` n `1250`
- 24h: commodity avg `-1.6897` n `13`; crypto_alt avg `2.7701` n `239`; crypto_major avg `2.6634` n `8`; equity avg `-0.4824` n `158`; fx avg `0.0497` n `6`; index avg `0.1745` n `27`; metal avg `1.1333` n `20`; unknown avg `0.2723` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2643`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
