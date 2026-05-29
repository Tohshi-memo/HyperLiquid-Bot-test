# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T16:52:20.469753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.718` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9128` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0387` n `12`; crypto_alt avg `-0.1155` n `228`; crypto_major avg `0.0806` n `8`; equity avg `-0.1028` n `69`; fx avg `0.0055` n `6`; index avg `-0.0313` n `23`; metal avg `-0.1279` n `18`; unknown avg `0.011` n `419`
- 1h: commodity avg `-0.3448` n `12`; crypto_alt avg `0.2452` n `228`; crypto_major avg `0.6183` n `8`; equity avg `0.1236` n `69`; fx avg `-0.0212` n `6`; index avg `0.0038` n `23`; metal avg `-0.0602` n `18`; unknown avg `0.2096` n `418`
- 4h: commodity avg `-0.644` n `12`; crypto_alt avg `2.0208` n `228`; crypto_major avg `2.074` n `8`; equity avg `0.6584` n `69`; fx avg `0.1027` n `6`; index avg `-0.1897` n `23`; metal avg `0.1612` n `18`; unknown avg `0.646` n `417`
- 24h: commodity avg `-0.3837` n `12`; crypto_alt avg `1.8468` n `228`; crypto_major avg `2.2962` n `8`; equity avg `2.0027` n `69`; fx avg `0.2028` n `6`; index avg `-0.193` n `23`; metal avg `0.1186` n `18`; unknown avg `1.3563` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1974`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
