# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T01:52:25.475879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.066` n `12`; crypto_alt avg `-0.0992` n `233`; crypto_major avg `0.0169` n `8`; equity avg `0.1391` n `134`; fx avg `0.002` n `6`; index avg `0.047` n `26`; metal avg `0.0123` n `20`; unknown avg `0.4029` n `797`
- 1h: commodity avg `-0.028` n `12`; crypto_alt avg `-0.6308` n `233`; crypto_major avg `-0.3837` n `8`; equity avg `-0.2571` n `134`; fx avg `0.0298` n `6`; index avg `-0.0322` n `26`; metal avg `-0.0079` n `20`; unknown avg `9.7275` n `795`
- 4h: commodity avg `-0.1136` n `12`; crypto_alt avg `-1.5905` n `233`; crypto_major avg `-0.808` n `8`; equity avg `-0.5102` n `134`; fx avg `0.0106` n `6`; index avg `-0.0375` n `26`; metal avg `-0.0145` n `20`; unknown avg `0.2524` n `735`
- 24h: commodity avg `0.006` n `12`; crypto_alt avg `-3.8334` n `233`; crypto_major avg `-2.6492` n `8`; equity avg `-1.3897` n `134`; fx avg `0.0228` n `6`; index avg `-0.2464` n `26`; metal avg `0.4163` n `20`; unknown avg `1.5808` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
