# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T03:22:21.903043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.0518` n `228`; crypto_major avg `0.0289` n `8`; equity avg `0.138` n `69`; fx avg `0.0006` n `6`; index avg `0.0284` n `23`; metal avg `-0.0677` n `18`; unknown avg `0.1342` n `417`
- 1h: commodity avg `-0.093` n `12`; crypto_alt avg `-0.3491` n `228`; crypto_major avg `0.1187` n `8`; equity avg `0.1746` n `69`; fx avg `-0.0022` n `6`; index avg `0.0198` n `23`; metal avg `-0.2471` n `18`; unknown avg `-0.1149` n `417`
- 4h: commodity avg `-0.3342` n `12`; crypto_alt avg `-0.0189` n `228`; crypto_major avg `-0.2269` n `8`; equity avg `0.0061` n `69`; fx avg `0.0685` n `6`; index avg `-0.0796` n `23`; metal avg `-0.0903` n `18`; unknown avg `-0.2523` n `417`
- 24h: commodity avg `-0.2081` n `12`; crypto_alt avg `-0.83` n `228`; crypto_major avg `0.8105` n `8`; equity avg `3.4182` n `69`; fx avg `0.0725` n `6`; index avg `1.1106` n `23`; metal avg `2.016` n `18`; unknown avg `0.3653` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
