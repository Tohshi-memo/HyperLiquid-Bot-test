# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T13:07:18.675013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.155` n `12`; crypto_alt avg `-0.2991` n `228`; crypto_major avg `-0.1645` n `8`; equity avg `0.012` n `69`; fx avg `0.0048` n `6`; index avg `-0.0187` n `23`; metal avg `0.0556` n `18`; unknown avg `0.0417` n `417`
- 1h: commodity avg `-0.0452` n `12`; crypto_alt avg `-0.4743` n `228`; crypto_major avg `-0.2128` n `8`; equity avg `0.0394` n `69`; fx avg `0.0197` n `6`; index avg `0.0251` n `23`; metal avg `0.0557` n `18`; unknown avg `-0.0985` n `417`
- 4h: commodity avg `-0.2458` n `12`; crypto_alt avg `-1.3345` n `228`; crypto_major avg `-0.7521` n `8`; equity avg `-0.1475` n `69`; fx avg `0.0268` n `6`; index avg `0.1389` n `23`; metal avg `0.2547` n `18`; unknown avg `-0.1948` n `417`
- 24h: commodity avg `0.0987` n `12`; crypto_alt avg `0.5396` n `228`; crypto_major avg `1.4315` n `8`; equity avg `2.937` n `69`; fx avg `0.0699` n `6`; index avg `1.1785` n `23`; metal avg `1.4914` n `18`; unknown avg `0.9998` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
