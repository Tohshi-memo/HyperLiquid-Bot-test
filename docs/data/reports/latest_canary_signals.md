# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T08:52:30.847680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3782` n `12`; crypto_alt avg `0.4184` n `234`; crypto_major avg `0.574` n `8`; equity avg `0.4274` n `140`; fx avg `-0.0684` n `6`; index avg `0.075` n `26`; metal avg `0.2273` n `20`; unknown avg `0.7365` n `944`
- 1h: commodity avg `-0.4781` n `12`; crypto_alt avg `0.7942` n `234`; crypto_major avg `0.9791` n `8`; equity avg `0.1054` n `140`; fx avg `-0.1663` n `6`; index avg `0.029` n `26`; metal avg `0.2042` n `20`; unknown avg `1.9138` n `936`
- 4h: commodity avg `-0.4996` n `12`; crypto_alt avg `0.9231` n `234`; crypto_major avg `0.7661` n `8`; equity avg `-0.2621` n `140`; fx avg `-0.118` n `6`; index avg `-0.0457` n `26`; metal avg `-0.0141` n `20`; unknown avg `9.3044` n `908`
- 24h: commodity avg `-0.6252` n `12`; crypto_alt avg `2.1125` n `234`; crypto_major avg `2.4766` n `8`; equity avg `0.7426` n `140`; fx avg `-0.2755` n `6`; index avg `0.2285` n `26`; metal avg `-0.0817` n `20`; unknown avg `1125.7535` n `792`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
