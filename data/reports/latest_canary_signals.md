# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T06:52:34.553687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `0.0065` n `234`; crypto_major avg `-0.0394` n `8`; equity avg `0.032` n `140`; fx avg `-0.0033` n `6`; index avg `0.0039` n `26`; metal avg `0.0335` n `20`; unknown avg `0.7104` n `930`
- 1h: commodity avg `-0.117` n `12`; crypto_alt avg `0.488` n `234`; crypto_major avg `0.1244` n `8`; equity avg `0.1468` n `140`; fx avg `-0.0418` n `6`; index avg `0.0428` n `26`; metal avg `0.0307` n `20`; unknown avg `0.154` n `896`
- 4h: commodity avg `0.0704` n `12`; crypto_alt avg `1.4189` n `234`; crypto_major avg `0.4272` n `8`; equity avg `0.1261` n `140`; fx avg `-0.0344` n `6`; index avg `0.0624` n `26`; metal avg `-0.0342` n `20`; unknown avg `0.0506` n `890`
- 24h: commodity avg `-0.61` n `12`; crypto_alt avg `4.1165` n `234`; crypto_major avg `2.8427` n `8`; equity avg `1.23` n `140`; fx avg `-0.0524` n `6`; index avg `0.2661` n `26`; metal avg `0.0027` n `20`; unknown avg `2.6161` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
