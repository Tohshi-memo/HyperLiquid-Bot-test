# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T09:22:30.377139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0468` n `12`; crypto_alt avg `0.0044` n `230`; crypto_major avg `-0.0099` n `8`; equity avg `0.0617` n `113`; fx avg `-0.0097` n `6`; index avg `0.0115` n `25`; metal avg `0.018` n `20`; unknown avg `-0.0041` n `787`
- 1h: commodity avg `-0.1641` n `12`; crypto_alt avg `0.1026` n `230`; crypto_major avg `0.1289` n `8`; equity avg `0.099` n `113`; fx avg `-0.0171` n `6`; index avg `0.0226` n `25`; metal avg `0.075` n `20`; unknown avg `0.0462` n `787`
- 4h: commodity avg `0.1164` n `12`; crypto_alt avg `-0.1223` n `230`; crypto_major avg `-0.2837` n `8`; equity avg `0.4257` n `113`; fx avg `-0.01` n `6`; index avg `0.0751` n `25`; metal avg `0.2631` n `20`; unknown avg `-0.0012` n `755`
- 24h: commodity avg `0.0473` n `12`; crypto_alt avg `-0.656` n `230`; crypto_major avg `-0.6197` n `8`; equity avg `1.8209` n `113`; fx avg `-0.0675` n `6`; index avg `0.3611` n `25`; metal avg `-0.0881` n `20`; unknown avg `0.9312` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2012`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1749`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
