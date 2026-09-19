# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T15:37:25.713260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0872` n `12`; crypto_alt avg `-0.0673` n `234`; crypto_major avg `0.0026` n `8`; equity avg `0.0037` n `140`; fx avg `0.0029` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.053` n `943`
- 1h: commodity avg `-0.157` n `12`; crypto_alt avg `-0.3053` n `234`; crypto_major avg `-0.0587` n `8`; equity avg `0.0029` n `140`; fx avg `-0.0042` n `6`; index avg `0.0051` n `26`; metal avg `0.0031` n `20`; unknown avg `0.3192` n `940`
- 4h: commodity avg `-0.1528` n `12`; crypto_alt avg `-0.0533` n `234`; crypto_major avg `0.3582` n `8`; equity avg `0.0407` n `140`; fx avg `-0.0281` n `6`; index avg `0.0181` n `26`; metal avg `0.0084` n `20`; unknown avg `0.5463` n `932`
- 24h: commodity avg `-0.3149` n `12`; crypto_alt avg `2.7062` n `234`; crypto_major avg `1.6414` n `8`; equity avg `0.7063` n `140`; fx avg `0.018` n `6`; index avg `0.1418` n `26`; metal avg `0.0761` n `20`; unknown avg `1.5952` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1711`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
