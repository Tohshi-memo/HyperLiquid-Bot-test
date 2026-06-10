# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T04:07:22.706009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0812` n `12`; crypto_alt avg `-0.0949` n `228`; crypto_major avg `-0.1614` n `8`; equity avg `-0.1209` n `74`; fx avg `0.0054` n `6`; index avg `-0.045` n `23`; metal avg `-0.0879` n `18`; unknown avg `-0.3998` n `547`
- 1h: commodity avg `-0.0015` n `12`; crypto_alt avg `-0.1191` n `228`; crypto_major avg `0.0519` n `8`; equity avg `-0.2858` n `74`; fx avg `0.0195` n `6`; index avg `-0.0559` n `23`; metal avg `0.1509` n `18`; unknown avg `-0.5784` n `547`
- 4h: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.9134` n `228`; crypto_major avg `-1.2172` n `8`; equity avg `-1.2052` n `74`; fx avg `0.0833` n `6`; index avg `-0.4122` n `23`; metal avg `-1.0828` n `18`; unknown avg `-0.8136` n `547`
- 24h: commodity avg `-0.5017` n `12`; crypto_alt avg `-0.0755` n `228`; crypto_major avg `-2.5969` n `8`; equity avg `-3.2615` n `74`; fx avg `0.1494` n `6`; index avg `-1.3629` n `23`; metal avg `-2.8795` n `18`; unknown avg `0.8212` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0482`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0428`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.041`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0409`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0399`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0382`, n `668`, weak_sample_signal
