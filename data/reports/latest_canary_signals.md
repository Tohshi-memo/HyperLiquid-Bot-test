# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T00:07:25.117147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0148` n `12`; crypto_alt avg `0.059` n `230`; crypto_major avg `-0.0464` n `8`; equity avg `-0.3199` n `98`; fx avg `0.0161` n `6`; index avg `-0.0772` n `25`; metal avg `-0.0358` n `20`; unknown avg `-0.0932` n `770`
- 1h: commodity avg `-0.0309` n `12`; crypto_alt avg `0.0682` n `230`; crypto_major avg `0.0332` n `8`; equity avg `-0.3401` n `98`; fx avg `0.0336` n `6`; index avg `-0.1375` n `25`; metal avg `-0.0301` n `20`; unknown avg `-0.3507` n `770`
- 4h: commodity avg `0.0182` n `12`; crypto_alt avg `0.067` n `230`; crypto_major avg `0.042` n `8`; equity avg `-0.3191` n `98`; fx avg `0.0084` n `6`; index avg `-0.151` n `25`; metal avg `-0.0507` n `20`; unknown avg `-0.5386` n `770`
- 24h: commodity avg `-0.3205` n `12`; crypto_alt avg `1.2134` n `230`; crypto_major avg `0.6844` n `8`; equity avg `-1.1582` n `98`; fx avg `-0.1926` n `6`; index avg `-0.2598` n `25`; metal avg `0.1312` n `20`; unknown avg `-0.1631` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1083`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0931`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0855`, n `666`, weak_sample_signal
