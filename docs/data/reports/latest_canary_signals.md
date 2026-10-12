# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T20:22:29.282985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0543` n `13`; crypto_alt avg `-0.0864` n `235`; crypto_major avg `-0.0316` n `8`; equity avg `-0.0251` n `151`; fx avg `-0.0026` n `6`; index avg `-0.0028` n `26`; metal avg `0.0086` n `20`; unknown avg `0.237` n `1134`
- 1h: commodity avg `-0.1688` n `13`; crypto_alt avg `0.2997` n `235`; crypto_major avg `0.4353` n `8`; equity avg `0.1271` n `151`; fx avg `-0.0129` n `6`; index avg `0.0106` n `26`; metal avg `0.0339` n `20`; unknown avg `20.1846` n `1106`
- 4h: commodity avg `-0.1874` n `13`; crypto_alt avg `-0.4889` n `235`; crypto_major avg `-0.3149` n `8`; equity avg `-0.2677` n `151`; fx avg `-0.0109` n `6`; index avg `-0.053` n `26`; metal avg `-0.0114` n `20`; unknown avg `0.9032` n `1106`
- 24h: commodity avg `0.1968` n `13`; crypto_alt avg `-2.8403` n `235`; crypto_major avg `-1.5024` n `8`; equity avg `-3.3768` n `151`; fx avg `-0.1789` n `6`; index avg `-0.3385` n `26`; metal avg `-0.1737` n `20`; unknown avg `0.0101` n `869`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2062`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.173`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1214`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1124`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1041`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0967`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0886`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `666`, weak_sample_signal
