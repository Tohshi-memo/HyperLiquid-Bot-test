# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T15:37:21.959578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `3.0071` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `1.719` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1365` n `12`; crypto_alt avg `1.0981` n `228`; crypto_major avg `0.765` n `8`; equity avg `0.2269` n `69`; fx avg `0.0151` n `6`; index avg `0.0114` n `23`; metal avg `-0.2049` n `18`; unknown avg `0.434` n `418`
- 1h: commodity avg `-0.633` n `12`; crypto_alt avg `2.8661` n `228`; crypto_major avg `2.3741` n `8`; equity avg `0.9765` n `69`; fx avg `0.1147` n `6`; index avg `0.14` n `23`; metal avg `0.6551` n `18`; unknown avg `3.6784` n `418`
- 4h: commodity avg `-0.331` n `12`; crypto_alt avg `1.6421` n `228`; crypto_major avg `1.6354` n `8`; equity avg `0.5609` n `69`; fx avg `0.1314` n `6`; index avg `-0.2567` n `23`; metal avg `0.2855` n `18`; unknown avg `0.6721` n `417`
- 24h: commodity avg `-0.5421` n `12`; crypto_alt avg `3.162` n `228`; crypto_major avg `3.2979` n `8`; equity avg `1.929` n `69`; fx avg `0.2127` n `6`; index avg `-0.0648` n `23`; metal avg `0.8913` n `18`; unknown avg `2.486` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
