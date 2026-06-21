# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T02:37:27.039213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.0248` n `228`; crypto_major avg `-0.01` n `8`; equity avg `0.0081` n `78`; fx avg `0.099` n `6`; index avg `-0.0167` n `23`; metal avg `0.013` n `18`; unknown avg `0.1951` n `702`
- 1h: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.1827` n `228`; crypto_major avg `-0.0658` n `8`; equity avg `0.0413` n `78`; fx avg `-0.0067` n `6`; index avg `0.0019` n `23`; metal avg `0.0258` n `18`; unknown avg `-0.0921` n `702`
- 4h: commodity avg `0.0254` n `12`; crypto_alt avg `0.1887` n `228`; crypto_major avg `-0.3007` n `8`; equity avg `0.0549` n `78`; fx avg `-0.0119` n `6`; index avg `-0.0211` n `23`; metal avg `-0.0317` n `18`; unknown avg `2.8023` n `701`
- 24h: commodity avg `0.2298` n `12`; crypto_alt avg `1.6346` n `228`; crypto_major avg `1.6581` n `8`; equity avg `0.4362` n `78`; fx avg `0.043` n `6`; index avg `-0.0002` n `23`; metal avg `-0.0225` n `18`; unknown avg `1.75` n `557`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
