# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T01:22:28.626805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1386` n `12`; crypto_alt avg `0.1581` n `228`; crypto_major avg `0.3631` n `8`; equity avg `0.1771` n `74`; fx avg `0.027` n `6`; index avg `0.1576` n `23`; metal avg `0.662` n `18`; unknown avg `0.0747` n `550`
- 1h: commodity avg `-0.0715` n `12`; crypto_alt avg `0.5438` n `228`; crypto_major avg `0.4986` n `8`; equity avg `0.9022` n `74`; fx avg `0.067` n `6`; index avg `0.4847` n `23`; metal avg `0.9231` n `18`; unknown avg `0.2002` n `550`
- 4h: commodity avg `0.0221` n `12`; crypto_alt avg `1.7048` n `228`; crypto_major avg `0.939` n `8`; equity avg `0.9563` n `74`; fx avg `0.1087` n `6`; index avg `0.4769` n `23`; metal avg `0.786` n `18`; unknown avg `0.1979` n `550`
- 24h: commodity avg `1.5399` n `12`; crypto_alt avg `-1.0585` n `228`; crypto_major avg `-1.2302` n `8`; equity avg `-1.2818` n `74`; fx avg `0.1305` n `6`; index avg `-1.1841` n `23`; metal avg `-0.8922` n `18`; unknown avg `-0.1128` n `537`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
