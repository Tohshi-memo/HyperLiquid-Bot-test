# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T10:37:29.734264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.1322` n `234`; crypto_major avg `0.0431` n `8`; equity avg `-0.0161` n `140`; fx avg `-0.0013` n `6`; index avg `-0.0121` n `26`; metal avg `0.0046` n `20`; unknown avg `0.0743` n `942`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.555` n `234`; crypto_major avg `0.324` n `8`; equity avg `0.0294` n `140`; fx avg `-0.0023` n `6`; index avg `-0.007` n `26`; metal avg `0.0114` n `20`; unknown avg `-0.1619` n `940`
- 4h: commodity avg `-0.0126` n `12`; crypto_alt avg `1.2512` n `234`; crypto_major avg `0.0666` n `8`; equity avg `0.025` n `140`; fx avg `0.0254` n `6`; index avg `0.0263` n `26`; metal avg `0.0037` n `20`; unknown avg `0.3213` n `934`
- 24h: commodity avg `0.219` n `12`; crypto_alt avg `3.1393` n `234`; crypto_major avg `3.1983` n `8`; equity avg `0.1303` n `140`; fx avg `-0.015` n `6`; index avg `-0.0479` n `26`; metal avg `-0.1607` n `20`; unknown avg `2.247` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
