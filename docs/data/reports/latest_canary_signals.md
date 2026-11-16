# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T21:22:28.625865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `13`; crypto_alt avg `0.0957` n `239`; crypto_major avg `0.0954` n `8`; equity avg `0.0518` n `162`; fx avg `-0.0026` n `6`; index avg `0.0093` n `27`; metal avg `0.0304` n `20`; unknown avg `0.7688` n `1266`
- 1h: commodity avg `-0.0249` n `13`; crypto_alt avg `-0.1079` n `239`; crypto_major avg `0.0682` n `8`; equity avg `-0.0571` n `162`; fx avg `-0.0226` n `6`; index avg `0.0009` n `27`; metal avg `-0.0365` n `20`; unknown avg `2.1568` n `1230`
- 4h: commodity avg `-0.2329` n `13`; crypto_alt avg `-0.2943` n `239`; crypto_major avg `-0.0593` n `8`; equity avg `-0.7106` n `162`; fx avg `-0.0591` n `6`; index avg `-0.1098` n `27`; metal avg `-0.1655` n `20`; unknown avg `12.9063` n `1221`
- 24h: commodity avg `-1.1932` n `13`; crypto_alt avg `0.2173` n `239`; crypto_major avg `0.3389` n `8`; equity avg `-3.3327` n `162`; fx avg `-0.1509` n `6`; index avg `-0.3282` n `27`; metal avg `-0.3565` n `20`; unknown avg `292.4864` n `1027`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
