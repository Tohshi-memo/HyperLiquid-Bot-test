# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T19:37:26.503646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.1679` n `234`; crypto_major avg `-0.0876` n `8`; equity avg `-0.0084` n `141`; fx avg `0.0117` n `6`; index avg `-0.0007` n `26`; metal avg `0.0016` n `20`; unknown avg `3.4893` n `961`
- 1h: commodity avg `-0.0235` n `12`; crypto_alt avg `-0.3748` n `234`; crypto_major avg `-0.1465` n `8`; equity avg `-0.0203` n `141`; fx avg `0.0036` n `6`; index avg `0.0013` n `26`; metal avg `0.0069` n `20`; unknown avg `3.5269` n `959`
- 4h: commodity avg `-0.0145` n `12`; crypto_alt avg `-1.2286` n `234`; crypto_major avg `-0.799` n `8`; equity avg `-0.0769` n `141`; fx avg `0.0024` n `6`; index avg `-0.0099` n `26`; metal avg `0.0029` n `20`; unknown avg `8.5651` n `945`
- 24h: commodity avg `0.3539` n `12`; crypto_alt avg `1.2901` n `234`; crypto_major avg `-0.7535` n `8`; equity avg `0.015` n `141`; fx avg `0.0176` n `6`; index avg `-0.0216` n `26`; metal avg `-0.056` n `20`; unknown avg `2.9994` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
