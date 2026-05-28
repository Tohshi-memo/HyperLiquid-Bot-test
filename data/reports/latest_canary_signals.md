# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T22:52:16.545077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.056` n `12`; crypto_alt avg `0.1369` n `228`; crypto_major avg `0.1182` n `8`; equity avg `0.0887` n `69`; fx avg `-0.0018` n `6`; index avg `0.0079` n `23`; metal avg `-0.0077` n `18`; unknown avg `0.0271` n `417`
- 1h: commodity avg `0.1172` n `12`; crypto_alt avg `-0.6537` n `228`; crypto_major avg `-0.4503` n `8`; equity avg `0.2002` n `69`; fx avg `0.0022` n `6`; index avg `0.0382` n `23`; metal avg `-0.0097` n `18`; unknown avg `-0.1518` n `417`
- 4h: commodity avg `-0.1794` n `12`; crypto_alt avg `-0.6736` n `228`; crypto_major avg `-0.3962` n `8`; equity avg `0.4264` n `69`; fx avg `-0.0044` n `6`; index avg `-0.1319` n `23`; metal avg `-0.039` n `18`; unknown avg `0.0175` n `417`
- 24h: commodity avg `0.9383` n `12`; crypto_alt avg `-2.0523` n `228`; crypto_major avg `-0.0238` n `8`; equity avg `2.2644` n `69`; fx avg `-0.0175` n `6`; index avg `0.7482` n `23`; metal avg `0.4775` n `18`; unknown avg `-0.2021` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
