# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T09:07:27.769993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `0.0583` n `228`; crypto_major avg `0.0639` n `8`; equity avg `-0.0161` n `78`; fx avg `0.0052` n `6`; index avg `-0.0042` n `23`; metal avg `0.005` n `18`; unknown avg `-0.0249` n `702`
- 1h: commodity avg `0.0435` n `12`; crypto_alt avg `-0.2145` n `228`; crypto_major avg `-0.2793` n `8`; equity avg `-0.0909` n `78`; fx avg `-0.0012` n `6`; index avg `-0.0125` n `23`; metal avg `-0.0299` n `18`; unknown avg `-0.1005` n `702`
- 4h: commodity avg `-0.0398` n `12`; crypto_alt avg `0.3455` n `228`; crypto_major avg `-0.4629` n `8`; equity avg `0.0019` n `78`; fx avg `-0.0056` n `6`; index avg `0.001` n `23`; metal avg `0.0168` n `18`; unknown avg `-0.1036` n `662`
- 24h: commodity avg `0.1` n `12`; crypto_alt avg `1.0617` n `228`; crypto_major avg `-0.2394` n `8`; equity avg `0.2713` n `78`; fx avg `0.3409` n `6`; index avg `0.037` n `23`; metal avg `-0.0246` n `18`; unknown avg `0.0786` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
