# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T19:37:29.936354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0343` n `12`; crypto_alt avg `0.0098` n `234`; crypto_major avg `0.0813` n `8`; equity avg `-0.0147` n `140`; fx avg `0.0052` n `6`; index avg `0.0` n `26`; metal avg `-0.0125` n `20`; unknown avg `6.7616` n `917`
- 1h: commodity avg `-0.1897` n `12`; crypto_alt avg `-0.0433` n `234`; crypto_major avg `0.1179` n `8`; equity avg `0.0018` n `140`; fx avg `-0.0032` n `6`; index avg `0.008` n `26`; metal avg `-0.0547` n `20`; unknown avg `21.8831` n `915`
- 4h: commodity avg `-0.0665` n `12`; crypto_alt avg `0.5155` n `234`; crypto_major avg `-0.0468` n `8`; equity avg `0.2304` n `140`; fx avg `0.0327` n `6`; index avg `0.0234` n `26`; metal avg `-0.1597` n `20`; unknown avg `2.279` n `909`
- 24h: commodity avg `-0.1427` n `12`; crypto_alt avg `4.7393` n `234`; crypto_major avg `2.1546` n `8`; equity avg `3.0644` n `138`; fx avg `0.0122` n `6`; index avg `0.5883` n `26`; metal avg `0.6474` n `20`; unknown avg `4.1013` n `749`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
