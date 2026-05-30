# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T07:07:15.494766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.1771` n `228`; crypto_major avg `-0.037` n `8`; equity avg `0.0003` n `69`; fx avg `-0.0001` n `6`; index avg `-0.034` n `23`; metal avg `0.0019` n `18`; unknown avg `-0.1477` n `421`
- 1h: commodity avg `0.0185` n `12`; crypto_alt avg `-0.2105` n `228`; crypto_major avg `0.0013` n `8`; equity avg `0.0285` n `69`; fx avg `0.0005` n `6`; index avg `0.0002` n `23`; metal avg `-0.0027` n `18`; unknown avg `-0.3254` n `421`
- 4h: commodity avg `-0.1083` n `12`; crypto_alt avg `-0.7131` n `228`; crypto_major avg `-0.1591` n `8`; equity avg `0.1265` n `69`; fx avg `0.005` n `6`; index avg `0.0994` n `23`; metal avg `-0.0175` n `18`; unknown avg `0.0073` n `401`
- 24h: commodity avg `-0.215` n `12`; crypto_alt avg `1.0576` n `228`; crypto_major avg `1.6656` n `8`; equity avg `0.7488` n `69`; fx avg `0.0345` n `6`; index avg `0.0653` n `23`; metal avg `-0.1646` n `18`; unknown avg `0.4463` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
