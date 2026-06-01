# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T07:07:20.863855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1176` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0285` n `12`; crypto_alt avg `0.0974` n `228`; crypto_major avg `0.0951` n `8`; equity avg `0.0631` n `69`; fx avg `0.0306` n `6`; index avg `0.0123` n `23`; metal avg `0.1166` n `18`; unknown avg `0.122` n `422`
- 1h: commodity avg `0.196` n `12`; crypto_alt avg `-0.3335` n `228`; crypto_major avg `0.0127` n `8`; equity avg `-0.1613` n `69`; fx avg `0.0267` n `6`; index avg `0.3846` n `23`; metal avg `-0.2234` n `18`; unknown avg `-0.063` n `422`
- 4h: commodity avg `0.2975` n `12`; crypto_alt avg `-1.7246` n `228`; crypto_major avg `-0.9374` n `8`; equity avg `-0.1975` n `69`; fx avg `-0.0618` n `6`; index avg `0.1802` n `23`; metal avg `-0.1458` n `18`; unknown avg `-0.3058` n `412`
- 24h: commodity avg `1.0856` n `12`; crypto_alt avg `-0.1871` n `228`; crypto_major avg `-0.7045` n `8`; equity avg `0.2411` n `69`; fx avg `-0.0334` n `6`; index avg `0.8583` n `23`; metal avg `0.0999` n `18`; unknown avg `1.5401` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2875`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2218`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
