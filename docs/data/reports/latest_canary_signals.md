# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T00:52:29.498690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.019` n `12`; crypto_alt avg `0.5399` n `228`; crypto_major avg `0.6252` n `8`; equity avg `0.2037` n `88`; fx avg `-0.001` n `6`; index avg `0.0502` n `23`; metal avg `0.0782` n `20`; unknown avg `0.3018` n `764`
- 1h: commodity avg `0.0621` n `12`; crypto_alt avg `-0.1709` n `228`; crypto_major avg `-0.3593` n `8`; equity avg `-0.7704` n `88`; fx avg `0.0407` n `6`; index avg `-0.2375` n `23`; metal avg `-0.0763` n `20`; unknown avg `1.781` n `764`
- 4h: commodity avg `-0.1548` n `12`; crypto_alt avg `-0.2935` n `228`; crypto_major avg `-0.2773` n `8`; equity avg `-0.6505` n `88`; fx avg `0.0278` n `6`; index avg `-0.2063` n `23`; metal avg `-0.2435` n `20`; unknown avg `0.4896` n `762`
- 24h: commodity avg `-0.404` n `12`; crypto_alt avg `-0.6006` n `228`; crypto_major avg `-0.7598` n `8`; equity avg `-0.352` n `88`; fx avg `-0.024` n `6`; index avg `-0.125` n `23`; metal avg `-0.2288` n `20`; unknown avg `15.576` n `690`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1879`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
