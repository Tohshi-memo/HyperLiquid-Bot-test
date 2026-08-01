# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T17:07:33.113371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0206` n `12`; crypto_alt avg `-0.0163` n `230`; crypto_major avg `0.019` n `8`; equity avg `0.0176` n `102`; fx avg `-0.0072` n `6`; index avg `0.0032` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.0363` n `782`
- 1h: commodity avg `0.1002` n `12`; crypto_alt avg `-0.0069` n `230`; crypto_major avg `0.0298` n `8`; equity avg `-0.0273` n `102`; fx avg `0.0055` n `6`; index avg `-0.0212` n `25`; metal avg `0.0014` n `20`; unknown avg `-0.0377` n `782`
- 4h: commodity avg `0.0558` n `12`; crypto_alt avg `-0.1332` n `230`; crypto_major avg `0.0148` n `8`; equity avg `-0.1159` n `102`; fx avg `0.0008` n `6`; index avg `-0.0134` n `25`; metal avg `0.0039` n `20`; unknown avg `-0.1537` n `782`
- 24h: commodity avg `0.6949` n `12`; crypto_alt avg `0.1714` n `230`; crypto_major avg `-0.3235` n `8`; equity avg `-0.7518` n `102`; fx avg `-0.1174` n `6`; index avg `-0.0883` n `25`; metal avg `0.0708` n `20`; unknown avg `4.3011` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
