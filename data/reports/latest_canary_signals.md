# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T13:52:28.012644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.072` n `12`; crypto_alt avg `0.1128` n `230`; crypto_major avg `0.1622` n `8`; equity avg `0.3556` n `98`; fx avg `-0.0116` n `6`; index avg `0.0481` n `25`; metal avg `0.1146` n `20`; unknown avg `0.0099` n `773`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `0.4846` n `230`; crypto_major avg `0.4128` n `8`; equity avg `1.1671` n `98`; fx avg `0.0092` n `6`; index avg `0.159` n `25`; metal avg `0.1757` n `20`; unknown avg `10.3421` n `773`
- 4h: commodity avg `-0.141` n `12`; crypto_alt avg `0.4278` n `230`; crypto_major avg `0.3772` n `8`; equity avg `0.8258` n `98`; fx avg `-0.0114` n `6`; index avg `0.1021` n `25`; metal avg `0.1881` n `20`; unknown avg `10.7993` n `773`
- 24h: commodity avg `0.4375` n `12`; crypto_alt avg `-0.3497` n `230`; crypto_major avg `-1.2119` n `8`; equity avg `0.7374` n `98`; fx avg `0.0086` n `6`; index avg `0.0463` n `25`; metal avg `0.7056` n `20`; unknown avg `0.8357` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1014`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.071`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.067`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.064`, n `666`, weak_sample_signal
