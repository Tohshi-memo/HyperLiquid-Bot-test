# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T12:22:26.633554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0623` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0091` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8725` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0163` n `13`; crypto_alt avg `0.3238` n `239`; crypto_major avg `0.3493` n `8`; equity avg `0.0672` n `166`; fx avg `0.0042` n `6`; index avg `0.0046` n `27`; metal avg `0.0289` n `20`; unknown avg `-0.1326` n `1260`
- 1h: commodity avg `0.0431` n `13`; crypto_alt avg `0.731` n `239`; crypto_major avg `1.003` n `8`; equity avg `0.1179` n `166`; fx avg `0.0102` n `6`; index avg `0.0069` n `27`; metal avg `0.0274` n `20`; unknown avg `165.751` n `1224`
- 4h: commodity avg `0.0482` n `13`; crypto_alt avg `1.3432` n `239`; crypto_major avg `2.1105` n `8`; equity avg `0.238` n `166`; fx avg `0.0411` n `6`; index avg `0.0185` n `27`; metal avg `0.1014` n `20`; unknown avg `165.2418` n `1224`
- 24h: commodity avg `0.5443` n `13`; crypto_alt avg `-4.042` n `239`; crypto_major avg `-4.1942` n `8`; equity avg `-3.7566` n `166`; fx avg `-0.088` n `6`; index avg `-0.4368` n `27`; metal avg `-0.36` n `20`; unknown avg `-0.3174` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
