# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T13:07:33.489421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0644` n `12`; crypto_alt avg `-0.022` n `230`; crypto_major avg `0.0109` n `8`; equity avg `-0.1102` n `102`; fx avg `-0.0069` n `6`; index avg `-0.007` n `25`; metal avg `-0.0618` n `20`; unknown avg `-0.0244` n `774`
- 1h: commodity avg `0.1387` n `12`; crypto_alt avg `-0.231` n `230`; crypto_major avg `-0.1483` n `8`; equity avg `-0.2324` n `102`; fx avg `-0.0133` n `6`; index avg `-0.0213` n `25`; metal avg `-0.1074` n `20`; unknown avg `-0.0518` n `774`
- 4h: commodity avg `0.3247` n `12`; crypto_alt avg `0.0425` n `230`; crypto_major avg `0.0614` n `8`; equity avg `-0.3913` n `102`; fx avg `-0.0368` n `6`; index avg `-0.0494` n `25`; metal avg `-0.1639` n `20`; unknown avg `-0.0303` n `773`
- 24h: commodity avg `-0.3856` n `12`; crypto_alt avg `0.5054` n `230`; crypto_major avg `1.3102` n `8`; equity avg `0.8516` n `102`; fx avg `0.0722` n `6`; index avg `0.098` n `25`; metal avg `0.2147` n `20`; unknown avg `-0.0602` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
