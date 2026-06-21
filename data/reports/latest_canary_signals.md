# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T08:37:37.943546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.1385` n `228`; crypto_major avg `-0.2302` n `8`; equity avg `-0.0387` n `78`; fx avg `0.0035` n `6`; index avg `-0.0018` n `23`; metal avg `-0.0098` n `18`; unknown avg `0.0157` n `702`
- 1h: commodity avg `-0.0163` n `12`; crypto_alt avg `-0.3664` n `228`; crypto_major avg `-0.6248` n `8`; equity avg `-0.1063` n `78`; fx avg `0.0961` n `6`; index avg `-0.0129` n `23`; metal avg `-0.0551` n `18`; unknown avg `-0.1889` n `694`
- 4h: commodity avg `-0.0925` n `12`; crypto_alt avg `-0.1207` n `228`; crypto_major avg `-0.9625` n `8`; equity avg `0.002` n `78`; fx avg `-0.0021` n `6`; index avg `0.0038` n `23`; metal avg `0.0118` n `18`; unknown avg `-0.1096` n `654`
- 24h: commodity avg `0.0337` n `12`; crypto_alt avg `1.0814` n `228`; crypto_major avg `-0.2352` n `8`; equity avg `0.2016` n `78`; fx avg `0.0506` n `6`; index avg `0.0089` n `23`; metal avg `-0.0378` n `18`; unknown avg `-0.0219` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
