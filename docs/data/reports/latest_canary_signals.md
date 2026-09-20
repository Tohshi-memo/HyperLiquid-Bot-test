# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T16:07:23.664303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0346` n `12`; crypto_alt avg `0.3733` n `234`; crypto_major avg `0.2295` n `8`; equity avg `0.043` n `140`; fx avg `-0.0306` n `6`; index avg `0.0004` n `26`; metal avg `-0.001` n `20`; unknown avg `2.6984` n `897`
- 1h: commodity avg `-0.0052` n `12`; crypto_alt avg `0.7221` n `234`; crypto_major avg `0.378` n `8`; equity avg `0.1354` n `140`; fx avg `-0.0268` n `6`; index avg `0.0014` n `26`; metal avg `-0.0024` n `20`; unknown avg `0.6461` n `897`
- 4h: commodity avg `-0.0069` n `12`; crypto_alt avg `0.8236` n `234`; crypto_major avg `0.632` n `8`; equity avg `0.1707` n `140`; fx avg `-0.019` n `6`; index avg `0.0051` n `26`; metal avg `0.0072` n `20`; unknown avg `1.3054` n `897`
- 24h: commodity avg `0.4106` n `12`; crypto_alt avg `-1.1107` n `234`; crypto_major avg `-1.5982` n `8`; equity avg `-0.1104` n `140`; fx avg `-0.0456` n `6`; index avg `-0.0469` n `26`; metal avg `-0.0262` n `20`; unknown avg `175.171` n `795`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
