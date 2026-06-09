# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T12:07:28.162266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0714` n `12`; crypto_alt avg `0.5858` n `228`; crypto_major avg `0.5578` n `8`; equity avg `-0.0203` n `74`; fx avg `0.0093` n `6`; index avg `-0.0205` n `23`; metal avg `0.1826` n `18`; unknown avg `0.0644` n `547`
- 1h: commodity avg `0.1171` n `12`; crypto_alt avg `0.7248` n `228`; crypto_major avg `0.3744` n `8`; equity avg `0.0378` n `74`; fx avg `0.0304` n `6`; index avg `-0.0134` n `23`; metal avg `0.3221` n `18`; unknown avg `-0.1782` n `547`
- 4h: commodity avg `-0.2751` n `12`; crypto_alt avg `0.5415` n `228`; crypto_major avg `0.1317` n `8`; equity avg `0.3801` n `74`; fx avg `0.1778` n `6`; index avg `0.3106` n `23`; metal avg `0.7534` n `18`; unknown avg `-0.1014` n `547`
- 24h: commodity avg `-0.2343` n `12`; crypto_alt avg `-0.1497` n `228`; crypto_major avg `0.3891` n `8`; equity avg `1.5296` n `74`; fx avg `0.1283` n `6`; index avg `0.7017` n `23`; metal avg `0.4229` n `18`; unknown avg `-2.9406` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
