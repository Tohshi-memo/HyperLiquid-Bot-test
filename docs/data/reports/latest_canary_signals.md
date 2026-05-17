# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T23:14:40.794023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0251` n `12`; crypto_alt avg `-0.186` n `228`; crypto_major avg `-0.0877` n `8`; equity avg `-0.3917` n `66`; fx avg `-0.0004` n `5`; index avg `-0.084` n `23`; metal avg `-0.1309` n `18`; unknown avg `0.9297` n `383`
- 1h: commodity avg `0.1613` n `12`; crypto_alt avg `-0.9041` n `228`; crypto_major avg `-0.851` n `8`; equity avg `-0.1478` n `66`; fx avg `-0.0009` n `5`; index avg `-0.1188` n `23`; metal avg `0.0772` n `18`; unknown avg `0.9317` n `383`
- 4h: commodity avg `0.0009` n `12`; crypto_alt avg `-0.714` n `228`; crypto_major avg `-0.4677` n `8`; equity avg `0.2165` n `66`; fx avg `-0.0188` n `5`; index avg `0.0485` n `23`; metal avg `0.5451` n `18`; unknown avg `0.0595` n `383`
- 24h: commodity avg `1.8864` n `12`; crypto_alt avg `-9.906` n `228`; crypto_major avg `-2.115` n `8`; equity avg `-2.5637` n `65`; fx avg `-0.1739` n `5`; index avg `-1.5396` n `23`; metal avg `-5.3936` n `18`; unknown avg `551.2644` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
