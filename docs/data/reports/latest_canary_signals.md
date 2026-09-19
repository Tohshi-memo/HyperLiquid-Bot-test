# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T14:37:27.785949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.1039` n `234`; crypto_major avg `-0.1684` n `8`; equity avg `-0.0044` n `140`; fx avg `-0.0025` n `6`; index avg `-0.0015` n `26`; metal avg `0.0006` n `20`; unknown avg `0.5454` n `942`
- 1h: commodity avg `0.006` n `12`; crypto_alt avg `0.2915` n `234`; crypto_major avg `0.2298` n `8`; equity avg `0.0109` n `140`; fx avg `0.0006` n `6`; index avg `-0.0009` n `26`; metal avg `0.0038` n `20`; unknown avg `1.5678` n `940`
- 4h: commodity avg `0.028` n `12`; crypto_alt avg `0.487` n `234`; crypto_major avg `0.551` n `8`; equity avg `0.046` n `140`; fx avg `-0.0301` n `6`; index avg `0.0065` n `26`; metal avg `0.0209` n `20`; unknown avg `0.6392` n `932`
- 24h: commodity avg `-0.1536` n `12`; crypto_alt avg `3.2509` n `234`; crypto_major avg `1.8824` n `8`; equity avg `0.8399` n `140`; fx avg `-0.0492` n `6`; index avg `0.1318` n `26`; metal avg `0.1149` n `20`; unknown avg `1.7013` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
