# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T16:06:21.593578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.0959` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0457` n `13`; crypto_alt avg `0.1591` n `237`; crypto_major avg `0.1509` n `8`; equity avg `-0.012` n `151`; fx avg `0.0208` n `6`; index avg `0.0009` n `26`; metal avg `-0.0555` n `20`; unknown avg `0.424` n `1225`
- 1h: commodity avg `-0.1237` n `13`; crypto_alt avg `0.0137` n `237`; crypto_major avg `0.0436` n `8`; equity avg `-0.4509` n `151`; fx avg `0.025` n `6`; index avg `0.0324` n `26`; metal avg `-0.0577` n `20`; unknown avg `0.3295` n `1181`
- 4h: commodity avg `-0.1082` n `13`; crypto_alt avg `-0.7019` n `237`; crypto_major avg `0.0921` n `8`; equity avg `-2.0038` n `151`; fx avg `0.0598` n `6`; index avg `-0.1211` n `26`; metal avg `-0.1637` n `20`; unknown avg `-0.2617` n `1083`
- 24h: commodity avg `0.3689` n `13`; crypto_alt avg `-4.7151` n `237`; crypto_major avg `-3.2985` n `8`; equity avg `-4.4024` n `151`; fx avg `-0.1415` n `6`; index avg `-0.5499` n `26`; metal avg `-0.9043` n `20`; unknown avg `1.9216` n `908`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
