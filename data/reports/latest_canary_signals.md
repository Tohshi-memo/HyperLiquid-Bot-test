# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T01:07:25.606036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `0.5525` n `228`; crypto_major avg `0.4951` n `8`; equity avg `0.0754` n `74`; fx avg `0.0034` n `6`; index avg `0.0145` n `23`; metal avg `0.0045` n `18`; unknown avg `0.0359` n `516`
- 1h: commodity avg `0.0653` n `12`; crypto_alt avg `0.8287` n `228`; crypto_major avg `0.6305` n `8`; equity avg `0.0448` n `74`; fx avg `0.0012` n `6`; index avg `-0.0387` n `23`; metal avg `0.0118` n `18`; unknown avg `0.1013` n `516`
- 4h: commodity avg `0.0942` n `12`; crypto_alt avg `1.4957` n `228`; crypto_major avg `0.8945` n `8`; equity avg `0.3538` n `74`; fx avg `-0.0335` n `6`; index avg `-0.0856` n `23`; metal avg `0.0784` n `18`; unknown avg `0.0524` n `515`
- 24h: commodity avg `0.0841` n `12`; crypto_alt avg `-1.051` n `228`; crypto_major avg `-1.5072` n `8`; equity avg `-0.3424` n `74`; fx avg `0.0217` n `6`; index avg `-0.1736` n `23`; metal avg `-0.3764` n `18`; unknown avg `0.4202` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
