# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T05:37:29.487218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `12`; crypto_alt avg `0.1565` n `234`; crypto_major avg `0.3202` n `8`; equity avg `0.025` n `141`; fx avg `-0.0` n `6`; index avg `-0.0062` n `26`; metal avg `0.0032` n `20`; unknown avg `0.7983` n `961`
- 1h: commodity avg `0.02` n `12`; crypto_alt avg `0.6727` n `234`; crypto_major avg `0.4034` n `8`; equity avg `0.0211` n `141`; fx avg `0.02` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0005` n `20`; unknown avg `1.56` n `959`
- 4h: commodity avg `0.0725` n `12`; crypto_alt avg `0.2487` n `234`; crypto_major avg `0.2673` n `8`; equity avg `0.1141` n `141`; fx avg `0.0137` n `6`; index avg `0.0107` n `26`; metal avg `-0.0133` n `20`; unknown avg `0.7656` n `949`
- 24h: commodity avg `0.0311` n `12`; crypto_alt avg `1.03` n `234`; crypto_major avg `0.1197` n `8`; equity avg `0.2742` n `141`; fx avg `0.0278` n `6`; index avg `0.0025` n `26`; metal avg `-0.012` n `20`; unknown avg `4.8355` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
