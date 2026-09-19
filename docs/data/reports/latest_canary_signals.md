# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T21:37:33.466967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.063` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0201` n `12`; crypto_alt avg `-0.3554` n `234`; crypto_major avg `-0.3579` n `8`; equity avg `-0.0152` n `140`; fx avg `0.0` n `6`; index avg `0.0129` n `26`; metal avg `-0.0061` n `20`; unknown avg `0.3961` n `943`
- 1h: commodity avg `0.0456` n `12`; crypto_alt avg `-1.06` n `234`; crypto_major avg `-0.8103` n `8`; equity avg `-0.0149` n `140`; fx avg `0.014` n `6`; index avg `0.027` n `26`; metal avg `-0.0048` n `20`; unknown avg `-0.2334` n `941`
- 4h: commodity avg `0.075` n `12`; crypto_alt avg `-1.0703` n `234`; crypto_major avg `-1.0312` n `8`; equity avg `0.1147` n `140`; fx avg `-0.0571` n `6`; index avg `0.0318` n `26`; metal avg `0.0116` n `20`; unknown avg `146.9708` n `919`
- 24h: commodity avg `0.1086` n `12`; crypto_alt avg `0.0524` n `234`; crypto_major avg `-0.7109` n `8`; equity avg `-0.0451` n `140`; fx avg `-0.0797` n `6`; index avg `0.0248` n `26`; metal avg `-0.0215` n `20`; unknown avg `5.3032` n `828`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
