# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T19:07:27.559428+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0471` n `12`; crypto_alt avg `-0.2005` n `233`; crypto_major avg `-0.3281` n `8`; equity avg `-0.1494` n `136`; fx avg `-0.0029` n `6`; index avg `-0.0278` n `27`; metal avg `-0.0175` n `20`; unknown avg `0.143` n `906`
- 1h: commodity avg `-0.1067` n `12`; crypto_alt avg `0.0135` n `233`; crypto_major avg `0.2139` n `8`; equity avg `-0.2858` n `136`; fx avg `-0.0221` n `6`; index avg `-0.0334` n `27`; metal avg `-0.0242` n `20`; unknown avg `0.3465` n `906`
- 4h: commodity avg `-0.2815` n `12`; crypto_alt avg `1.4417` n `233`; crypto_major avg `1.5484` n `8`; equity avg `0.7362` n `136`; fx avg `-0.0073` n `6`; index avg `0.1545` n `27`; metal avg `0.137` n `20`; unknown avg `0.8667` n `878`
- 24h: commodity avg `0.1011` n `12`; crypto_alt avg `0.1323` n `233`; crypto_major avg `2.1487` n `8`; equity avg `-0.4504` n `136`; fx avg `0.0399` n `6`; index avg `-0.1476` n `27`; metal avg `-0.3439` n `20`; unknown avg `4.0157` n `696`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
