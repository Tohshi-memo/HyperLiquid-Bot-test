# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T07:22:28.023873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.0153` n `229`; crypto_major avg `0.0527` n `8`; equity avg `0.0205` n `91`; fx avg `-0.0373` n `6`; index avg `0.0125` n `25`; metal avg `0.0315` n `20`; unknown avg `-0.0069` n `763`
- 1h: commodity avg `0.0239` n `12`; crypto_alt avg `0.3506` n `229`; crypto_major avg `0.5916` n `8`; equity avg `0.2545` n `91`; fx avg `-0.0278` n `6`; index avg `0.0156` n `25`; metal avg `0.0786` n `20`; unknown avg `0.0601` n `763`
- 4h: commodity avg `0.1991` n `12`; crypto_alt avg `0.172` n `229`; crypto_major avg `0.3022` n `8`; equity avg `0.1306` n `91`; fx avg `0.0263` n `6`; index avg `-0.0195` n `25`; metal avg `-0.0899` n `20`; unknown avg `13.1313` n `745`
- 24h: commodity avg `0.3417` n `12`; crypto_alt avg `0.639` n `229`; crypto_major avg `0.0048` n `8`; equity avg `-1.2131` n `90`; fx avg `-0.0491` n `6`; index avg `-0.3167` n `25`; metal avg `-0.3843` n `20`; unknown avg `-0.3911` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
