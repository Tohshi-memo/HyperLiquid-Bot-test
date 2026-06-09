# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T11:37:22.026526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1483` n `12`; crypto_alt avg `0.1474` n `228`; crypto_major avg `0.1101` n `8`; equity avg `0.0609` n `74`; fx avg `-0.0076` n `6`; index avg `-0.0357` n `23`; metal avg `-0.0503` n `18`; unknown avg `0.0487` n `547`
- 1h: commodity avg `0.1489` n `12`; crypto_alt avg `0.1114` n `228`; crypto_major avg `-0.0953` n `8`; equity avg `0.1742` n `74`; fx avg `0.0307` n `6`; index avg `0.0785` n `23`; metal avg `0.0182` n `18`; unknown avg `-0.1646` n `547`
- 4h: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.448` n `228`; crypto_major avg `-0.6428` n `8`; equity avg `0.2288` n `74`; fx avg `0.1925` n `6`; index avg `0.3297` n `23`; metal avg `0.4565` n `18`; unknown avg `-0.2492` n `547`
- 24h: commodity avg `-0.2585` n `12`; crypto_alt avg `-1.7074` n `228`; crypto_major avg `-1.0872` n `8`; equity avg `1.2996` n `74`; fx avg `0.095` n `6`; index avg `0.7045` n `23`; metal avg `0.3275` n `18`; unknown avg `-3.1508` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
