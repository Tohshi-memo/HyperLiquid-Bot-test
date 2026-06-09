# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T08:24:46.421451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1447` n `12`; crypto_alt avg `0.2512` n `228`; crypto_major avg `0.1846` n `8`; equity avg `0.1557` n `74`; fx avg `0.0238` n `6`; index avg `0.1434` n `23`; metal avg `0.3886` n `18`; unknown avg `0.0565` n `547`
- 1h: commodity avg `0.0573` n `12`; crypto_alt avg `-0.3589` n `228`; crypto_major avg `-0.5249` n `8`; equity avg `-0.1178` n `74`; fx avg `0.0554` n `6`; index avg `0.0656` n `23`; metal avg `0.4085` n `18`; unknown avg `-0.012` n `547`
- 4h: commodity avg `0.0624` n `12`; crypto_alt avg `1.0166` n `228`; crypto_major avg `0.6332` n `8`; equity avg `0.2492` n `74`; fx avg `0.1033` n `6`; index avg `0.1951` n `23`; metal avg `0.6434` n `18`; unknown avg `0.4228` n `503`
- 24h: commodity avg `-1.1256` n `12`; crypto_alt avg `0.4598` n `228`; crypto_major avg `0.9926` n `8`; equity avg `2.1687` n `74`; fx avg `0.0113` n `6`; index avg `1.1124` n `23`; metal avg `1.1262` n `18`; unknown avg `-2.58` n `503`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
