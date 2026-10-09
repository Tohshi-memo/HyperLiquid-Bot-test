# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T16:52:32.001593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0505` n `13`; crypto_alt avg `0.3035` n `235`; crypto_major avg `0.1529` n `8`; equity avg `0.0598` n `150`; fx avg `-0.0027` n `6`; index avg `0.0149` n `26`; metal avg `0.0295` n `20`; unknown avg `0.0199` n `1084`
- 1h: commodity avg `-0.1404` n `13`; crypto_alt avg `0.3365` n `235`; crypto_major avg `0.0596` n `8`; equity avg `0.0908` n `150`; fx avg `-0.0281` n `6`; index avg `0.0243` n `26`; metal avg `-0.0334` n `20`; unknown avg `1.5575` n `1076`
- 4h: commodity avg `0.1297` n `13`; crypto_alt avg `0.6597` n `235`; crypto_major avg `-0.1165` n `8`; equity avg `-0.2144` n `150`; fx avg `0.0104` n `6`; index avg `0.004` n `26`; metal avg `0.1184` n `20`; unknown avg `-0.1217` n `996`
- 24h: commodity avg `0.1544` n `13`; crypto_alt avg `3.5491` n `235`; crypto_major avg `1.9621` n `8`; equity avg `1.0971` n `150`; fx avg `0.0203` n `6`; index avg `0.1712` n `26`; metal avg `0.6939` n `20`; unknown avg `2.5486` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
