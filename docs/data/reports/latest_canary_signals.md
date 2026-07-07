# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T00:52:25.743607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.0033` n `229`; crypto_major avg `0.067` n `8`; equity avg `0.081` n `91`; fx avg `-0.021` n `6`; index avg `0.0221` n `25`; metal avg `0.0013` n `20`; unknown avg `0.5657` n `763`
- 1h: commodity avg `0.0254` n `12`; crypto_alt avg `0.1644` n `229`; crypto_major avg `0.3734` n `8`; equity avg `-0.1886` n `91`; fx avg `-0.01` n `6`; index avg `-0.0864` n `25`; metal avg `-0.1102` n `20`; unknown avg `0.54` n `763`
- 4h: commodity avg `0.0628` n `12`; crypto_alt avg `0.2296` n `229`; crypto_major avg `0.3704` n `8`; equity avg `-0.7463` n `91`; fx avg `0.0103` n `6`; index avg `-0.1914` n `25`; metal avg `-0.1465` n `20`; unknown avg `1.3102` n `763`
- 24h: commodity avg `0.3329` n `12`; crypto_alt avg `0.5379` n `229`; crypto_major avg `-0.1841` n `8`; equity avg `-1.3127` n `90`; fx avg `0.1045` n `6`; index avg `-0.2637` n `25`; metal avg `-0.4146` n `20`; unknown avg `-0.3081` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
