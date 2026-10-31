# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T12:52:30.756338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `13`; crypto_alt avg `-0.0154` n `238`; crypto_major avg `-0.1062` n `8`; equity avg `-0.0428` n `156`; fx avg `-0.0048` n `6`; index avg `-0.0058` n `27`; metal avg `-0.0067` n `20`; unknown avg `0.1118` n `1262`
- 1h: commodity avg `0.0093` n `13`; crypto_alt avg `0.3342` n `238`; crypto_major avg `0.0462` n `8`; equity avg `-0.0687` n `156`; fx avg `-0.0035` n `6`; index avg `-0.0065` n `27`; metal avg `-0.0045` n `20`; unknown avg `0.7989` n `1250`
- 4h: commodity avg `0.002` n `13`; crypto_alt avg `0.5802` n `238`; crypto_major avg `0.569` n `8`; equity avg `-0.0024` n `156`; fx avg `-0.0078` n `6`; index avg `-0.0148` n `27`; metal avg `0.027` n `20`; unknown avg `16.5385` n `1218`
- 24h: commodity avg `-0.1491` n `13`; crypto_alt avg `0.7557` n `238`; crypto_major avg `-0.3522` n `8`; equity avg `-1.0125` n `156`; fx avg `-0.019` n `6`; index avg `-0.1118` n `27`; metal avg `-0.1747` n `20`; unknown avg `3.9638` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
