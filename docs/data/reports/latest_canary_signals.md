# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T08:37:29.983300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `-0.0158` n `230`; crypto_major avg `0.0039` n `8`; equity avg `0.1462` n `98`; fx avg `-0.0119` n `6`; index avg `0.0152` n `25`; metal avg `-0.0126` n `20`; unknown avg `-0.0074` n `771`
- 1h: commodity avg `-0.083` n `12`; crypto_alt avg `-0.0481` n `230`; crypto_major avg `0.1796` n `8`; equity avg `0.4137` n `98`; fx avg `0.0229` n `6`; index avg `0.0322` n `25`; metal avg `-0.0815` n `20`; unknown avg `-0.0117` n `771`
- 4h: commodity avg `0.0002` n `12`; crypto_alt avg `0.4294` n `230`; crypto_major avg `0.721` n `8`; equity avg `0.85` n `98`; fx avg `0.0572` n `6`; index avg `0.047` n `25`; metal avg `0.3316` n `20`; unknown avg `0.0707` n `755`
- 24h: commodity avg `0.1545` n `12`; crypto_alt avg `2.94` n `230`; crypto_major avg `3.2046` n `8`; equity avg `2.1649` n `98`; fx avg `-0.0776` n `6`; index avg `0.3371` n `25`; metal avg `0.5533` n `20`; unknown avg `0.2211` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0751`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
