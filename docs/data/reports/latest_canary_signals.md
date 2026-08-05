# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T22:07:36.563714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0819` n `12`; crypto_alt avg `0.0482` n `230`; crypto_major avg `-0.0429` n `8`; equity avg `0.1424` n `108`; fx avg `-0.0071` n `6`; index avg `0.016` n `25`; metal avg `0.0006` n `20`; unknown avg `0.0559` n `782`
- 1h: commodity avg `-0.0649` n `12`; crypto_alt avg `-0.1263` n `230`; crypto_major avg `-0.2049` n `8`; equity avg `-0.1192` n `108`; fx avg `-0.0049` n `6`; index avg `-0.0214` n `25`; metal avg `-0.0043` n `20`; unknown avg `-0.018` n `782`
- 4h: commodity avg `-0.0576` n `12`; crypto_alt avg `-0.2388` n `230`; crypto_major avg `-0.5293` n `8`; equity avg `-1.1131` n `108`; fx avg `0.0049` n `6`; index avg `-0.1161` n `25`; metal avg `-0.0733` n `20`; unknown avg `0.0329` n `782`
- 24h: commodity avg `-0.0016` n `12`; crypto_alt avg `0.4532` n `230`; crypto_major avg `0.5554` n `8`; equity avg `-0.8286` n `108`; fx avg `-0.048` n `6`; index avg `-0.115` n `25`; metal avg `0.7998` n `20`; unknown avg `0.7702` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
