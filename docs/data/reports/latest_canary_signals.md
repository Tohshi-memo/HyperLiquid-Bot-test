# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T16:37:25.564450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0107` n `12`; crypto_alt avg `0.1106` n `234`; crypto_major avg `0.0301` n `8`; equity avg `0.0025` n `140`; fx avg `0.001` n `6`; index avg `0.0009` n `26`; metal avg `-0.004` n `20`; unknown avg `-0.046` n `943`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `0.3627` n `234`; crypto_major avg `0.072` n `8`; equity avg `0.0139` n `140`; fx avg `-0.0054` n `6`; index avg `0.0092` n `26`; metal avg `-0.0141` n `20`; unknown avg `4.4134` n `925`
- 4h: commodity avg `-0.1533` n `12`; crypto_alt avg `0.2222` n `234`; crypto_major avg `0.316` n `8`; equity avg `0.0499` n `140`; fx avg `-0.0069` n `6`; index avg `0.0118` n `26`; metal avg `-0.0083` n `20`; unknown avg `4.6408` n `922`
- 24h: commodity avg `-0.1232` n `12`; crypto_alt avg `2.5467` n `234`; crypto_major avg `1.2387` n `8`; equity avg `0.7885` n `140`; fx avg `0.0207` n `6`; index avg `0.1784` n `26`; metal avg `-0.0665` n `20`; unknown avg `2.9785` n `806`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
