# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T22:37:16.968769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0457` n `12`; crypto_alt avg `-0.2788` n `228`; crypto_major avg `-0.1624` n `8`; equity avg `-0.0885` n `69`; fx avg `0.0019` n `6`; index avg `-0.0735` n `23`; metal avg `0.0141` n `18`; unknown avg `-0.2107` n `417`
- 1h: commodity avg `0.2965` n `12`; crypto_alt avg `-0.8654` n `228`; crypto_major avg `-0.596` n `8`; equity avg `0.1661` n `69`; fx avg `0.0026` n `6`; index avg `-0.0259` n `23`; metal avg `-0.0071` n `18`; unknown avg `-0.3114` n `417`
- 4h: commodity avg `-0.1748` n `12`; crypto_alt avg `-0.6138` n `228`; crypto_major avg `-0.2338` n `8`; equity avg `0.4316` n `69`; fx avg `-0.0089` n `6`; index avg `-0.1484` n `23`; metal avg `-0.0468` n `18`; unknown avg `-0.0033` n `417`
- 24h: commodity avg `0.9208` n `12`; crypto_alt avg `-2.4166` n `228`; crypto_major avg `-0.4201` n `8`; equity avg `2.1743` n `69`; fx avg `-0.009` n `6`; index avg `0.7352` n `23`; metal avg `0.4252` n `18`; unknown avg `-0.3879` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
