# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T20:07:27.995525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0449` n `12`; crypto_alt avg `0.211` n `228`; crypto_major avg `0.0683` n `8`; equity avg `0.473` n `74`; fx avg `-0.0248` n `6`; index avg `0.333` n `23`; metal avg `0.0712` n `18`; unknown avg `0.2751` n `547`
- 1h: commodity avg `0.1243` n `12`; crypto_alt avg `0.2446` n `228`; crypto_major avg `0.0744` n `8`; equity avg `0.1896` n `74`; fx avg `-0.0415` n `6`; index avg `0.1998` n `23`; metal avg `-0.2235` n `18`; unknown avg `0.2356` n `547`
- 4h: commodity avg `0.5678` n `12`; crypto_alt avg `1.9406` n `228`; crypto_major avg `1.2333` n `8`; equity avg `2.0397` n `74`; fx avg `-0.0932` n `6`; index avg `1.0622` n `23`; metal avg `0.029` n `18`; unknown avg `0.7204` n `547`
- 24h: commodity avg `-0.8088` n `12`; crypto_alt avg `-1.6783` n `228`; crypto_major avg `-2.7027` n `8`; equity avg `-1.7323` n `74`; fx avg `0.0482` n `6`; index avg `-0.8756` n `23`; metal avg `-1.3978` n `18`; unknown avg `-1.1624` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0429`, n `668`, weak_sample_signal
