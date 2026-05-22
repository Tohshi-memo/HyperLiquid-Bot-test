# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T11:07:14.759961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0521` n `12`; crypto_alt avg `0.1339` n `228`; crypto_major avg `0.0565` n `8`; equity avg `0.0632` n `67`; fx avg `-0.0031` n `6`; index avg `0.0529` n `23`; metal avg `0.0289` n `18`; unknown avg `-0.0232` n `386`
- 1h: commodity avg `0.0351` n `12`; crypto_alt avg `0.1568` n `228`; crypto_major avg `-0.0` n `8`; equity avg `-0.0062` n `67`; fx avg `-0.0214` n `6`; index avg `-0.0814` n `23`; metal avg `-0.1811` n `18`; unknown avg `0.0248` n `386`
- 4h: commodity avg `0.1115` n `12`; crypto_alt avg `0.5232` n `228`; crypto_major avg `0.5851` n `8`; equity avg `-0.4846` n `67`; fx avg `-0.0066` n `6`; index avg `-0.1783` n `23`; metal avg `0.1219` n `18`; unknown avg `-0.0947` n `386`
- 24h: commodity avg `-1.0065` n `12`; crypto_alt avg `2.6249` n `228`; crypto_major avg `0.9287` n `8`; equity avg `1.4256` n `67`; fx avg `0.0646` n `6`; index avg `0.8918` n `23`; metal avg `0.9313` n `18`; unknown avg `1.1109` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.043`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0425`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0377`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0369`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0358`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0327`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0321`, n `668`, weak_sample_signal
