# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T12:52:31.137195+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1169` n `12`; crypto_alt avg `-0.1243` n `228`; crypto_major avg `-0.0808` n `8`; equity avg `-0.0652` n `74`; fx avg `-0.0088` n `6`; index avg `-0.0536` n `23`; metal avg `-0.0552` n `18`; unknown avg `-0.1374` n `547`
- 1h: commodity avg `0.0371` n `12`; crypto_alt avg `0.3093` n `228`; crypto_major avg `0.1994` n `8`; equity avg `-0.0833` n `74`; fx avg `0.0286` n `6`; index avg `-0.0405` n `23`; metal avg `0.0643` n `18`; unknown avg `-0.0387` n `547`
- 4h: commodity avg `0.208` n `12`; crypto_alt avg `-0.176` n `228`; crypto_major avg `-0.6886` n `8`; equity avg `0.0551` n `74`; fx avg `0.1632` n `6`; index avg `0.0759` n `23`; metal avg `0.4167` n `18`; unknown avg `-0.0952` n `547`
- 24h: commodity avg `-0.1769` n `12`; crypto_alt avg `-1.0971` n `228`; crypto_major avg `-0.7926` n `8`; equity avg `1.1187` n `74`; fx avg `0.1707` n `6`; index avg `0.5398` n `23`; metal avg `0.4444` n `18`; unknown avg `-0.6751` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
