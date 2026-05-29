# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T02:52:17.646523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `-0.3573` n `228`; crypto_major avg `-0.1734` n `8`; equity avg `-0.0732` n `69`; fx avg `0.0004` n `6`; index avg `-0.002` n `23`; metal avg `0.0395` n `18`; unknown avg `-0.239` n `417`
- 1h: commodity avg `-0.0971` n `12`; crypto_alt avg `-0.5712` n `228`; crypto_major avg `-0.4425` n `8`; equity avg `-0.0697` n `69`; fx avg `-0.0122` n `6`; index avg `0.0042` n `23`; metal avg `-0.0756` n `18`; unknown avg `-0.3826` n `417`
- 4h: commodity avg `-0.2672` n `12`; crypto_alt avg `-0.1214` n `228`; crypto_major avg `-0.5453` n `8`; equity avg `-0.1418` n `69`; fx avg `0.0674` n `6`; index avg `-0.067` n `23`; metal avg `0.1395` n `18`; unknown avg `-0.4321` n `417`
- 24h: commodity avg `0.2146` n `12`; crypto_alt avg `-1.7036` n `228`; crypto_major avg `-0.1104` n `8`; equity avg `2.7525` n `69`; fx avg `0.0459` n `6`; index avg `0.9723` n `23`; metal avg `1.8481` n `18`; unknown avg `-0.0195` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
