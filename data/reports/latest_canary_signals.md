# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T12:07:25.087469+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `0.1592` n `229`; crypto_major avg `0.1299` n `8`; equity avg `0.4021` n `91`; fx avg `0.0033` n `6`; index avg `0.0701` n `25`; metal avg `0.1078` n `20`; unknown avg `0.0926` n `763`
- 1h: commodity avg `-0.0521` n `12`; crypto_alt avg `0.7077` n `229`; crypto_major avg `0.5294` n `8`; equity avg `0.6743` n `91`; fx avg `-0.0027` n `6`; index avg `0.161` n `25`; metal avg `0.2187` n `20`; unknown avg `0.3051` n `763`
- 4h: commodity avg `0.4032` n `12`; crypto_alt avg `-0.3022` n `229`; crypto_major avg `-0.2466` n `8`; equity avg `-0.8217` n `91`; fx avg `-0.0002` n `6`; index avg `-0.151` n `25`; metal avg `-0.8154` n `20`; unknown avg `0.0625` n `763`
- 24h: commodity avg `1.3958` n `12`; crypto_alt avg `-3.6272` n `229`; crypto_major avg `-3.1037` n `8`; equity avg `-2.4511` n `91`; fx avg `-0.0979` n `6`; index avg `-0.5383` n `25`; metal avg `-1.3468` n `20`; unknown avg `-0.7427` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
