# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T11:07:27.848222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3459` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2636` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0005` n `13`; crypto_alt avg `0.1405` n `239`; crypto_major avg `0.2323` n `8`; equity avg `0.0763` n `166`; fx avg `0.0003` n `6`; index avg `0.0052` n `27`; metal avg `0.0061` n `20`; unknown avg `160.3922` n `1253`
- 1h: commodity avg `-0.0191` n `13`; crypto_alt avg `0.0927` n `239`; crypto_major avg `-0.0181` n `8`; equity avg `0.1314` n `166`; fx avg `0.0027` n `6`; index avg `0.0138` n `27`; metal avg `0.0226` n `20`; unknown avg `159.9877` n `1257`
- 4h: commodity avg `0.0694` n `13`; crypto_alt avg `2.1467` n `239`; crypto_major avg `2.4153` n `8`; equity avg `1.181` n `166`; fx avg `-0.0323` n `6`; index avg `0.1256` n `27`; metal avg `0.1517` n `20`; unknown avg `215.0033` n `1139`
- 24h: commodity avg `0.0684` n `13`; crypto_alt avg `3.4564` n `239`; crypto_major avg `4.1974` n `8`; equity avg `1.9165` n `166`; fx avg `-0.0066` n `6`; index avg `0.2328` n `27`; metal avg `0.1777` n `20`; unknown avg `0.0913` n `1054`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
