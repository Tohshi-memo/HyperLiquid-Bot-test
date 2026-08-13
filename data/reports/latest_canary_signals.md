# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T15:37:31.203384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.038` n `12`; crypto_alt avg `-0.1711` n `230`; crypto_major avg `-0.2949` n `8`; equity avg `-0.1884` n `113`; fx avg `0.005` n `6`; index avg `-0.0749` n `25`; metal avg `-0.0156` n `20`; unknown avg `-0.0752` n `787`
- 1h: commodity avg `0.2973` n `12`; crypto_alt avg `-0.2286` n `230`; crypto_major avg `-0.3243` n `8`; equity avg `-0.2537` n `113`; fx avg `0.0124` n `6`; index avg `-0.0593` n `25`; metal avg `-0.0406` n `20`; unknown avg `-0.023` n `787`
- 4h: commodity avg `0.0651` n `12`; crypto_alt avg `0.3193` n `230`; crypto_major avg `0.4367` n `8`; equity avg `1.4461` n `113`; fx avg `-0.0166` n `6`; index avg `0.2375` n `25`; metal avg `-0.1705` n `20`; unknown avg `-0.0032` n `787`
- 24h: commodity avg `-0.324` n `12`; crypto_alt avg `-0.0359` n `230`; crypto_major avg `0.1074` n `8`; equity avg `1.7688` n `113`; fx avg `-0.0009` n `6`; index avg `0.3091` n `25`; metal avg `-0.554` n `20`; unknown avg `0.2752` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2273`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2016`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1967`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1935`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
