# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T22:07:31.791182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0213` n `12`; crypto_alt avg `0.034` n `234`; crypto_major avg `0.1626` n `8`; equity avg `0.0226` n `140`; fx avg `-0.0131` n `6`; index avg `-0.003` n `26`; metal avg `-0.0077` n `20`; unknown avg `20.3054` n `930`
- 1h: commodity avg `0.0191` n `12`; crypto_alt avg `0.0659` n `234`; crypto_major avg `-0.0891` n `8`; equity avg `0.0457` n `140`; fx avg `-0.0233` n `6`; index avg `0.001` n `26`; metal avg `0.0058` n `20`; unknown avg `28.7165` n `914`
- 4h: commodity avg `-0.0725` n `12`; crypto_alt avg `1.1359` n `234`; crypto_major avg `0.6567` n `8`; equity avg `0.6437` n `140`; fx avg `0.0446` n `6`; index avg `0.1258` n `26`; metal avg `-0.1147` n `20`; unknown avg `4.6822` n `872`
- 24h: commodity avg `-0.0739` n `12`; crypto_alt avg `7.2553` n `234`; crypto_major avg `7.1708` n `8`; equity avg `1.3751` n `140`; fx avg `0.2321` n `6`; index avg `0.057` n `26`; metal avg `0.3663` n `20`; unknown avg `6.1873` n `711`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
