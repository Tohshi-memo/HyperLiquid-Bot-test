# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T12:07:27.916518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.0215` n `228`; crypto_major avg `0.048` n `8`; equity avg `0.0029` n `78`; fx avg `0.0126` n `6`; index avg `-0.0023` n `23`; metal avg `0.0051` n `18`; unknown avg `0.0522` n `573`
- 1h: commodity avg `-0.0403` n `12`; crypto_alt avg `0.0393` n `228`; crypto_major avg `0.2267` n `8`; equity avg `0.0633` n `78`; fx avg `0.011` n `6`; index avg `-0.0024` n `23`; metal avg `0.0136` n `18`; unknown avg `0.3587` n `573`
- 4h: commodity avg `-0.0885` n `12`; crypto_alt avg `0.3805` n `228`; crypto_major avg `0.4015` n `8`; equity avg `-0.1215` n `78`; fx avg `0.0245` n `6`; index avg `0.0212` n `23`; metal avg `-0.019` n `18`; unknown avg `-0.1493` n `573`
- 24h: commodity avg `0.4293` n `12`; crypto_alt avg `-2.9913` n `228`; crypto_major avg `-3.1818` n `8`; equity avg `1.1795` n `78`; fx avg `-0.065` n `6`; index avg `0.2914` n `23`; metal avg `-4.0928` n `18`; unknown avg `-0.0449` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
