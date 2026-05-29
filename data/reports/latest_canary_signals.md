# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T17:07:25.925629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6217` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9834` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `-0.0592` n `228`; crypto_major avg `-0.0833` n `8`; equity avg `0.1122` n `69`; fx avg `0.0045` n `6`; index avg `0.1657` n `23`; metal avg `0.0659` n `18`; unknown avg `-0.062` n `419`
- 1h: commodity avg `-0.4145` n `12`; crypto_alt avg `-0.0582` n `228`; crypto_major avg `0.2964` n `8`; equity avg `0.0216` n `69`; fx avg `-0.0062` n `6`; index avg `0.1265` n `23`; metal avg `0.0488` n `18`; unknown avg `-0.1628` n `419`
- 4h: commodity avg `-0.4669` n `12`; crypto_alt avg `2.2698` n `228`; crypto_major avg `2.1548` n `8`; equity avg `0.7637` n `69`; fx avg `0.1024` n `6`; index avg `-0.0091` n `23`; metal avg `0.1714` n `18`; unknown avg `0.577` n `417`
- 24h: commodity avg `-0.6314` n `12`; crypto_alt avg `1.8131` n `228`; crypto_major avg `2.219` n `8`; equity avg `1.9523` n `69`; fx avg `0.2091` n `6`; index avg `-0.0169` n `23`; metal avg `0.2406` n `18`; unknown avg `1.3195` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1978`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
