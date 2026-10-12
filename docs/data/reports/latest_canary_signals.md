# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T20:37:23.766193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `13`; crypto_alt avg `0.0335` n `235`; crypto_major avg `-0.0265` n `8`; equity avg `0.0007` n `151`; fx avg `-0.0012` n `6`; index avg `-0.0166` n `26`; metal avg `0.0069` n `20`; unknown avg `-0.0826` n `1134`
- 1h: commodity avg `-0.1546` n `13`; crypto_alt avg `0.0522` n `235`; crypto_major avg `0.1421` n `8`; equity avg `-0.0418` n `151`; fx avg `-0.0062` n `6`; index avg `-0.0251` n `26`; metal avg `0.0169` n `20`; unknown avg `8.6186` n `1106`
- 4h: commodity avg `-0.2127` n `13`; crypto_alt avg `-0.3617` n `235`; crypto_major avg `-0.2176` n `8`; equity avg `-0.1737` n `151`; fx avg `-0.0075` n `6`; index avg `-0.0623` n `26`; metal avg `0.0017` n `20`; unknown avg `0.4482` n `1106`
- 24h: commodity avg `0.1994` n `13`; crypto_alt avg `-2.882` n `235`; crypto_major avg `-1.5475` n `8`; equity avg `-3.3923` n `151`; fx avg `-0.178` n `6`; index avg `-0.3532` n `26`; metal avg `-0.1686` n `20`; unknown avg `-0.0007` n `869`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2073`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1718`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1206`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.108`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1028`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0971`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0885`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.076`, n `666`, weak_sample_signal
