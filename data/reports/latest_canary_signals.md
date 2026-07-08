# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T06:22:26.411940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.1957` n `229`; crypto_major avg `-0.2916` n `8`; equity avg `0.0233` n `91`; fx avg `-0.0366` n `6`; index avg `-0.01` n `25`; metal avg `0.0908` n `20`; unknown avg `-0.1107` n `763`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.3178` n `229`; crypto_major avg `-0.4803` n `8`; equity avg `-0.0902` n `91`; fx avg `-0.0367` n `6`; index avg `-0.0496` n `25`; metal avg `0.0825` n `20`; unknown avg `-0.1181` n `743`
- 4h: commodity avg `0.1005` n `12`; crypto_alt avg `-0.0028` n `229`; crypto_major avg `-0.4105` n `8`; equity avg `-0.2326` n `91`; fx avg `-0.0938` n `6`; index avg `-0.1848` n `25`; metal avg `0.2244` n `20`; unknown avg `-0.1529` n `743`
- 24h: commodity avg `0.8425` n `12`; crypto_alt avg `-2.7234` n `229`; crypto_major avg `-2.3236` n `8`; equity avg `-1.5462` n `91`; fx avg `-0.2728` n `6`; index avg `-0.3554` n `25`; metal avg `0.156` n `20`; unknown avg `-0.6136` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
