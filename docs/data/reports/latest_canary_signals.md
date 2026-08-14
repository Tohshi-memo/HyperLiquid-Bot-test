# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T13:36:09.593917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0906` n `12`; crypto_alt avg `0.0229` n `230`; crypto_major avg `0.0182` n `8`; equity avg `-0.4792` n `114`; fx avg `0.0026` n `6`; index avg `-0.0621` n `25`; metal avg `0.048` n `20`; unknown avg `0.0043` n `786`
- 1h: commodity avg `-0.1277` n `12`; crypto_alt avg `0.1901` n `230`; crypto_major avg `-0.1623` n `8`; equity avg `-0.6624` n `114`; fx avg `0.0309` n `6`; index avg `-0.0847` n `25`; metal avg `0.0565` n `20`; unknown avg `-0.102` n `786`
- 4h: commodity avg `-0.2555` n `12`; crypto_alt avg `0.0569` n `230`; crypto_major avg `-0.3044` n `8`; equity avg `-0.3424` n `114`; fx avg `0.028` n `6`; index avg `-0.0441` n `25`; metal avg `0.1591` n `20`; unknown avg `4.8141` n `786`
- 24h: commodity avg `-0.0599` n `12`; crypto_alt avg `-0.7349` n `230`; crypto_major avg `-1.234` n `8`; equity avg `0.2621` n `114`; fx avg `-0.0265` n `6`; index avg `0.1561` n `25`; metal avg `0.1025` n `20`; unknown avg `0.8867` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2079`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
