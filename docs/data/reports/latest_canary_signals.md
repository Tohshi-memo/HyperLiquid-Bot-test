# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T09:37:30.544508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0484` n `12`; crypto_alt avg `-0.0451` n `230`; crypto_major avg `-0.0458` n `8`; equity avg `0.0735` n `113`; fx avg `0.002` n `6`; index avg `0.0125` n `25`; metal avg `0.0173` n `20`; unknown avg `-0.0783` n `787`
- 1h: commodity avg `-0.0277` n `12`; crypto_alt avg `0.0074` n `230`; crypto_major avg `-0.1819` n `8`; equity avg `0.0179` n `113`; fx avg `-0.0278` n `6`; index avg `0.0073` n `25`; metal avg `0.06` n `20`; unknown avg `-0.0804` n `787`
- 4h: commodity avg `-0.2668` n `12`; crypto_alt avg `-0.0968` n `230`; crypto_major avg `-0.2783` n `8`; equity avg `-0.7647` n `113`; fx avg `0.0724` n `6`; index avg `-0.0645` n `25`; metal avg `-0.2419` n `20`; unknown avg `-0.1891` n `755`
- 24h: commodity avg `-0.24` n `12`; crypto_alt avg `-0.6912` n `230`; crypto_major avg `-0.3973` n `8`; equity avg `1.1321` n `113`; fx avg `0.0494` n `6`; index avg `0.1044` n `25`; metal avg `-0.5902` n `20`; unknown avg `0.1222` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2402`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1894`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1712`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
