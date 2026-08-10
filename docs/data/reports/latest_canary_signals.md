# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T15:44:31.922573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0807` n `12`; crypto_alt avg `0.1331` n `230`; crypto_major avg `0.046` n `8`; equity avg `0.0672` n `113`; fx avg `0.0001` n `6`; index avg `-0.0107` n `25`; metal avg `0.0127` n `20`; unknown avg `0.0261` n `784`
- 1h: commodity avg `0.1691` n `12`; crypto_alt avg `-0.4974` n `230`; crypto_major avg `-0.6387` n `8`; equity avg `-0.4546` n `113`; fx avg `-0.0082` n `6`; index avg `-0.0727` n `25`; metal avg `0.0323` n `20`; unknown avg `1.7739` n `784`
- 4h: commodity avg `0.5277` n `12`; crypto_alt avg `-0.6584` n `230`; crypto_major avg `-0.9445` n `8`; equity avg `-0.7527` n `113`; fx avg `0.0331` n `6`; index avg `-0.0596` n `25`; metal avg `0.1346` n `20`; unknown avg `1.5586` n `784`
- 24h: commodity avg `1.142` n `12`; crypto_alt avg `-0.3804` n `230`; crypto_major avg `-1.3934` n `8`; equity avg `-1.1865` n `113`; fx avg `0.2529` n `6`; index avg `-0.0471` n `25`; metal avg `-0.0765` n `20`; unknown avg `103.5222` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
