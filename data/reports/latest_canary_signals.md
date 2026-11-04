# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T17:57:47.611722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.3832` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.2244` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.875` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.2757` n `13`; crypto_alt avg `0.0237` n `239`; crypto_major avg `0.0704` n `8`; equity avg `0.0994` n `158`; fx avg `-0.0095` n `6`; index avg `0.0173` n `27`; metal avg `-0.0163` n `20`; unknown avg `0.3511` n `1260`
- 1h: commodity avg `0.1129` n `13`; crypto_alt avg `-0.9082` n `239`; crypto_major avg `-0.6455` n `8`; equity avg `0.2773` n `158`; fx avg `0.0131` n `6`; index avg `0.0138` n `27`; metal avg `0.0895` n `20`; unknown avg `-0.2908` n `1256`
- 4h: commodity avg `-1.1955` n `13`; crypto_alt avg `1.2857` n `239`; crypto_major avg `2.1877` n `8`; equity avg `-0.0367` n `158`; fx avg `-0.0612` n `6`; index avg `0.1202` n `27`; metal avg `0.3127` n `20`; unknown avg `0.5298` n `1250`
- 24h: commodity avg `-1.6052` n `13`; crypto_alt avg `1.9795` n `239`; crypto_major avg `1.9799` n `8`; equity avg `-0.4278` n `158`; fx avg `0.0553` n `6`; index avg `0.1637` n `27`; metal avg `1.2238` n `20`; unknown avg `0.0501` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2741`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
