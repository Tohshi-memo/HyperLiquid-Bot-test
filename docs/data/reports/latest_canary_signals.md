# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T12:07:33.325212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `-0.0417` n `234`; crypto_major avg `-0.0872` n `8`; equity avg `-0.0092` n `141`; fx avg `-0.0094` n `6`; index avg `-0.0027` n `26`; metal avg `0.0054` n `20`; unknown avg `5.9657` n `949`
- 1h: commodity avg `0.0068` n `12`; crypto_alt avg `-0.0468` n `234`; crypto_major avg `0.0775` n `8`; equity avg `0.0147` n `141`; fx avg `0.0072` n `6`; index avg `-0.005` n `26`; metal avg `0.009` n `20`; unknown avg `3.1482` n `949`
- 4h: commodity avg `-0.0247` n `12`; crypto_alt avg `0.6238` n `234`; crypto_major avg `0.125` n `8`; equity avg `0.0478` n `141`; fx avg `0.0166` n `6`; index avg `-0.0022` n `26`; metal avg `0.0031` n `20`; unknown avg `0.2682` n `949`
- 24h: commodity avg `0.2122` n `12`; crypto_alt avg `1.661` n `234`; crypto_major avg `-1.2166` n `8`; equity avg `-0.8889` n `141`; fx avg `-0.0235` n `6`; index avg `-0.0213` n `26`; metal avg `-0.0803` n `20`; unknown avg `1123.3809` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
