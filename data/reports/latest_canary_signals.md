# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T03:37:27.233392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `13`; crypto_alt avg `-0.8574` n `236`; crypto_major avg `-0.5674` n `8`; equity avg `-0.3457` n `151`; fx avg `-0.001` n `6`; index avg `-0.054` n `26`; metal avg `-0.0631` n `20`; unknown avg `1.8283` n `1136`
- 1h: commodity avg `0.0259` n `13`; crypto_alt avg `-0.8233` n `236`; crypto_major avg `-0.5617` n `8`; equity avg `-0.2812` n `151`; fx avg `0.005` n `6`; index avg `-0.0531` n `26`; metal avg `0.0012` n `20`; unknown avg `1.9233` n `1134`
- 4h: commodity avg `-0.0831` n `13`; crypto_alt avg `-0.6438` n `236`; crypto_major avg `-0.4695` n `8`; equity avg `0.1131` n `151`; fx avg `0.0602` n `6`; index avg `0.0084` n `26`; metal avg `0.1363` n `20`; unknown avg `0.8905` n `1128`
- 24h: commodity avg `-0.1261` n `13`; crypto_alt avg `3.0009` n `236`; crypto_major avg `1.7494` n `8`; equity avg `1.9141` n `151`; fx avg `0.0159` n `6`; index avg `0.3404` n `26`; metal avg `0.384` n `20`; unknown avg `25.7433` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.0949`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0896`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0871`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0761`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0718`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0661`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
