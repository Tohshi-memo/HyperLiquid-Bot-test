# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T08:37:17.013481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `0.0211` n `228`; crypto_major avg `0.0276` n `8`; equity avg `-0.0485` n `69`; fx avg `-0.166` n `6`; index avg `-0.0976` n `23`; metal avg `-0.0749` n `18`; unknown avg `0.0844` n `421`
- 1h: commodity avg `-0.0352` n `12`; crypto_alt avg `0.1284` n `228`; crypto_major avg `0.0778` n `8`; equity avg `-0.0175` n `69`; fx avg `-0.181` n `6`; index avg `-0.096` n `23`; metal avg `-0.0768` n `18`; unknown avg `-0.2174` n `421`
- 4h: commodity avg `0.0151` n `12`; crypto_alt avg `0.9586` n `228`; crypto_major avg `1.0056` n `8`; equity avg `0.2669` n `69`; fx avg `-0.1757` n `6`; index avg `0.0367` n `23`; metal avg `-0.0138` n `18`; unknown avg `-0.0659` n `401`
- 24h: commodity avg `-0.8253` n `12`; crypto_alt avg `1.4468` n `228`; crypto_major avg `1.6822` n `8`; equity avg `1.0115` n `69`; fx avg `-0.12` n `6`; index avg `0.0464` n `23`; metal avg `0.1994` n `18`; unknown avg `0.0788` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
