# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T23:37:36.435528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `0.1557` n `230`; crypto_major avg `0.1823` n `8`; equity avg `0.0553` n `98`; fx avg `-0.0005` n `6`; index avg `0.0125` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.0274` n `771`
- 1h: commodity avg `-0.0096` n `12`; crypto_alt avg `0.0151` n `230`; crypto_major avg `-0.0086` n `8`; equity avg `0.2219` n `98`; fx avg `0.002` n `6`; index avg `0.0103` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.1224` n `771`
- 4h: commodity avg `0.0312` n `12`; crypto_alt avg `-0.0696` n `230`; crypto_major avg `-0.1938` n `8`; equity avg `0.7642` n `98`; fx avg `-0.0175` n `6`; index avg `0.0298` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.2517` n `771`
- 24h: commodity avg `0.473` n `12`; crypto_alt avg `0.7343` n `230`; crypto_major avg `0.5828` n `8`; equity avg `4.4514` n `98`; fx avg `0.0599` n `6`; index avg `0.6182` n `25`; metal avg `0.7757` n `20`; unknown avg `0.3829` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.089`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0501`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0498`, n `666`, weak_sample_signal
