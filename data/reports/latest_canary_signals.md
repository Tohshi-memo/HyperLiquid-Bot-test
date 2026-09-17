# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T21:52:30.568071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.0501` n `234`; crypto_major avg `-0.1193` n `8`; equity avg `0.0036` n `140`; fx avg `-0.0098` n `6`; index avg `0.0086` n `26`; metal avg `0.018` n `20`; unknown avg `4.9744` n `919`
- 1h: commodity avg `0.0065` n `12`; crypto_alt avg `-0.0675` n `234`; crypto_major avg `-0.1296` n `8`; equity avg `0.0499` n `140`; fx avg `-0.0204` n `6`; index avg `0.0141` n `26`; metal avg `0.0262` n `20`; unknown avg `1.5375` n `887`
- 4h: commodity avg `-0.2167` n `12`; crypto_alt avg `0.0129` n `234`; crypto_major avg `-0.0099` n `8`; equity avg `0.1299` n `140`; fx avg `-0.0186` n `6`; index avg `-0.0107` n `26`; metal avg `-0.1414` n `20`; unknown avg `1.6182` n `857`
- 24h: commodity avg `-0.1994` n `12`; crypto_alt avg `3.8564` n `234`; crypto_major avg `1.9191` n `8`; equity avg `2.2999` n `138`; fx avg `-0.0296` n `6`; index avg `0.4473` n `26`; metal avg `0.576` n `20`; unknown avg `2.9086` n `763`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
