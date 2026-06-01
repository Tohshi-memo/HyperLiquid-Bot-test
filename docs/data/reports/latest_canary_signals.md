# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T18:37:34.159467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.34` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `2.21` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1686` n `12`; crypto_alt avg `0.294` n `228`; crypto_major avg `0.4429` n `8`; equity avg `-0.0191` n `69`; fx avg `-0.003` n `6`; index avg `0.0283` n `23`; metal avg `-0.0772` n `18`; unknown avg `0.9527` n `422`
- 1h: commodity avg `0.216` n `12`; crypto_alt avg `0.5327` n `228`; crypto_major avg `0.3769` n `8`; equity avg `0.0699` n `69`; fx avg `0.0176` n `6`; index avg `0.3952` n `23`; metal avg `0.1177` n `18`; unknown avg `1.0676` n `422`
- 4h: commodity avg `-0.9797` n `12`; crypto_alt avg `2.5702` n `228`; crypto_major avg `1.3603` n `8`; equity avg `1.4717` n `69`; fx avg `0.105` n `6`; index avg `0.8451` n `23`; metal avg `0.7178` n `18`; unknown avg `0.5256` n `422`
- 24h: commodity avg `0.2529` n `12`; crypto_alt avg `2.0437` n `228`; crypto_major avg `-0.1621` n `8`; equity avg `0.6173` n `69`; fx avg `0.0439` n `6`; index avg `0.7194` n `23`; metal avg `0.1315` n `18`; unknown avg `4.633` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3002`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2507`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2362`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
