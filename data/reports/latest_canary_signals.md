# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T22:39:54.630816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.2638` n `230`; crypto_major avg `-0.3016` n `8`; equity avg `-0.0911` n `102`; fx avg `0.006` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0083` n `20`; unknown avg `1.8056` n `774`
- 1h: commodity avg `-0.0417` n `12`; crypto_alt avg `-0.5152` n `230`; crypto_major avg `-0.6017` n `8`; equity avg `-0.3664` n `102`; fx avg `0.0042` n `6`; index avg `-0.0371` n `25`; metal avg `-0.034` n `20`; unknown avg `1.7022` n `774`
- 4h: commodity avg `-0.1967` n `12`; crypto_alt avg `-0.2788` n `230`; crypto_major avg `-0.4433` n `8`; equity avg `0.6946` n `102`; fx avg `-0.0165` n `6`; index avg `0.107` n `25`; metal avg `0.0336` n `20`; unknown avg `1470.5813` n `774`
- 24h: commodity avg `-0.6069` n `12`; crypto_alt avg `-2.3797` n `230`; crypto_major avg `-2.0413` n `8`; equity avg `-1.7461` n `102`; fx avg `-0.0393` n `6`; index avg `-0.4886` n `25`; metal avg `-0.0535` n `20`; unknown avg `1503.2184` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
