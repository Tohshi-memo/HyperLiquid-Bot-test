# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T15:37:31.691482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0534` n `12`; crypto_alt avg `0.312` n `230`; crypto_major avg `0.2586` n `8`; equity avg `0.3191` n `96`; fx avg `0.0301` n `6`; index avg `0.0674` n `25`; metal avg `0.0325` n `20`; unknown avg `0.0414` n `769`
- 1h: commodity avg `-0.0357` n `12`; crypto_alt avg `-0.0669` n `230`; crypto_major avg `-0.0117` n `8`; equity avg `-0.3317` n `96`; fx avg `0.0698` n `6`; index avg `0.0224` n `25`; metal avg `0.1556` n `20`; unknown avg `-0.1287` n `769`
- 4h: commodity avg `0.1923` n `12`; crypto_alt avg `-0.0579` n `230`; crypto_major avg `-0.1944` n `8`; equity avg `0.4741` n `96`; fx avg `0.057` n `6`; index avg `0.1172` n `25`; metal avg `0.2031` n `20`; unknown avg `0.0144` n `769`
- 24h: commodity avg `0.4754` n `12`; crypto_alt avg `-2.1714` n `230`; crypto_major avg `-3.1266` n `8`; equity avg `-2.6688` n `94`; fx avg `0.0507` n `6`; index avg `-0.46` n `25`; metal avg `-0.4204` n `20`; unknown avg `-0.3909` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
