# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T06:07:28.969950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0403` n `12`; crypto_alt avg `0.0796` n `230`; crypto_major avg `0.0813` n `8`; equity avg `0.0548` n `112`; fx avg `0.023` n `6`; index avg `0.0215` n `25`; metal avg `0.0707` n `20`; unknown avg `-0.0037` n `766`
- 1h: commodity avg `-0.0457` n `12`; crypto_alt avg `0.457` n `230`; crypto_major avg `0.2085` n `8`; equity avg `0.1888` n `112`; fx avg `0.0222` n `6`; index avg `0.0232` n `25`; metal avg `0.2134` n `20`; unknown avg `-0.0126` n `766`
- 4h: commodity avg `0.0696` n `12`; crypto_alt avg `0.0175` n `230`; crypto_major avg `-0.3641` n `8`; equity avg `0.4017` n `112`; fx avg `0.0142` n `6`; index avg `0.0502` n `25`; metal avg `0.1401` n `20`; unknown avg `-0.048` n `766`
- 24h: commodity avg `0.6175` n `12`; crypto_alt avg `0.4017` n `230`; crypto_major avg `-1.2038` n `8`; equity avg `1.1234` n `109`; fx avg `0.037` n `6`; index avg `-0.0652` n `25`; metal avg `0.1483` n `20`; unknown avg `110.8079` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
