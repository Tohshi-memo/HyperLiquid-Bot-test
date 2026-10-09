# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T03:22:34.589418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `13`; crypto_alt avg `0.4038` n `235`; crypto_major avg `0.1313` n `8`; equity avg `0.04` n `150`; fx avg `0.004` n `6`; index avg `-0.0004` n `26`; metal avg `0.0148` n `20`; unknown avg `-0.0124` n `1078`
- 1h: commodity avg `-0.0243` n `13`; crypto_alt avg `0.6372` n `235`; crypto_major avg `0.3505` n `8`; equity avg `-0.0823` n `150`; fx avg `-0.0011` n `6`; index avg `0.0001` n `26`; metal avg `0.016` n `20`; unknown avg `0.1842` n `1076`
- 4h: commodity avg `-0.1093` n `13`; crypto_alt avg `0.8241` n `235`; crypto_major avg `0.342` n `8`; equity avg `0.2609` n `150`; fx avg `0.0289` n `6`; index avg `0.0697` n `26`; metal avg `0.3483` n `20`; unknown avg `0.9523` n `1069`
- 24h: commodity avg `0.1776` n `13`; crypto_alt avg `-1.8923` n `235`; crypto_major avg `-2.6935` n `8`; equity avg `-2.0684` n `150`; fx avg `0.101` n `6`; index avg `-0.2096` n `26`; metal avg `0.1036` n `20`; unknown avg `6.666` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
