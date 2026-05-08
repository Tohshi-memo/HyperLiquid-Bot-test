# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T19:07:25.775176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0521` n `12`; crypto_alt avg `-0.0701` n `228`; crypto_major avg `-0.1092` n `8`; equity avg `0.0482` n `65`; fx avg `-0.001` n `5`; index avg `-0.0128` n `23`; metal avg `-0.0091` n `18`; unknown avg `0.441` n `375`
- 1h: commodity avg `0.0869` n `12`; crypto_alt avg `0.321` n `228`; crypto_major avg `0.3119` n `8`; equity avg `0.2156` n `65`; fx avg `0.012` n `5`; index avg `-0.1176` n `23`; metal avg `-0.1264` n `18`; unknown avg `0.066` n `375`
- 4h: commodity avg `-0.2599` n `12`; crypto_alt avg `1.7587` n `228`; crypto_major avg `1.3597` n `8`; equity avg `0.5765` n `65`; fx avg `0.029` n `5`; index avg `0.2999` n `23`; metal avg `0.0154` n `18`; unknown avg `0.0613` n `375`
- 24h: commodity avg `-0.0022` n `12`; crypto_alt avg `3.4058` n `228`; crypto_major avg `1.5237` n `8`; equity avg `3.3548` n `65`; fx avg `0.1899` n `5`; index avg `1.5389` n `23`; metal avg `0.7974` n `18`; unknown avg `0.7952` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1234`, n `664`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1194`, n `664`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.094`, n `664`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0933`, n `664`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0637`, n `664`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0578`, n `664`, weak_sample_signal
