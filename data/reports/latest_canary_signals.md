# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T02:22:30.173053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `0.0568` n `230`; crypto_major avg `0.114` n `8`; equity avg `0.0007` n `114`; fx avg `0.0043` n `6`; index avg `0.0003` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.0319` n `791`
- 1h: commodity avg `0.048` n `12`; crypto_alt avg `-0.1866` n `230`; crypto_major avg `0.0446` n `8`; equity avg `0.0382` n `114`; fx avg `0.0006` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.0044` n `791`
- 4h: commodity avg `0.0975` n `12`; crypto_alt avg `-0.6565` n `230`; crypto_major avg `-0.1597` n `8`; equity avg `0.0285` n `114`; fx avg `0.0025` n `6`; index avg `0.0163` n `25`; metal avg `0.0006` n `20`; unknown avg `-0.052` n `791`
- 24h: commodity avg `0.0033` n `12`; crypto_alt avg `-0.1619` n `230`; crypto_major avg `-0.0673` n `8`; equity avg `0.1604` n `114`; fx avg `0.0443` n `6`; index avg `0.0141` n `25`; metal avg `-0.0203` n `20`; unknown avg `-0.0046` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2229`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
