# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T15:52:26.496951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1296` n `12`; crypto_alt avg `-0.0059` n `230`; crypto_major avg `-0.0158` n `8`; equity avg `0.0455` n `98`; fx avg `-0.0028` n `6`; index avg `0.0268` n `25`; metal avg `0.0724` n `20`; unknown avg `-0.0199` n `773`
- 1h: commodity avg `-0.1607` n `12`; crypto_alt avg `0.3255` n `230`; crypto_major avg `0.3918` n `8`; equity avg `0.4818` n `98`; fx avg `0.0004` n `6`; index avg `0.1117` n `25`; metal avg `0.1321` n `20`; unknown avg `-0.1198` n `773`
- 4h: commodity avg `-0.2197` n `12`; crypto_alt avg `0.3872` n `230`; crypto_major avg `0.4102` n `8`; equity avg `1.3675` n `98`; fx avg `-0.0184` n `6`; index avg `0.2566` n `25`; metal avg `0.2339` n `20`; unknown avg `9.465` n `773`
- 24h: commodity avg `0.2856` n `12`; crypto_alt avg `-0.1807` n `230`; crypto_major avg `-0.897` n `8`; equity avg `0.3914` n `98`; fx avg `-0.0275` n `6`; index avg `-0.0026` n `25`; metal avg `0.527` n `20`; unknown avg `1.081` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1051`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.091`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0707`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0704`, n `666`, weak_sample_signal
