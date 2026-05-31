# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T20:02:24.251734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.091` n `12`; crypto_alt avg `0.2` n `228`; crypto_major avg `0.1947` n `8`; equity avg `0.0166` n `69`; fx avg `0.0018` n `6`; index avg `-0.0513` n `23`; metal avg `-0.0084` n `18`; unknown avg `0.0896` n `421`
- 1h: commodity avg `-0.0899` n `12`; crypto_alt avg `0.3315` n `228`; crypto_major avg `0.1936` n `8`; equity avg `0.0839` n `69`; fx avg `0.0039` n `6`; index avg `0.0221` n `23`; metal avg `-0.0196` n `18`; unknown avg `0.0872` n `421`
- 4h: commodity avg `-0.0254` n `12`; crypto_alt avg `0.1814` n `228`; crypto_major avg `-0.2247` n `8`; equity avg `0.0346` n `69`; fx avg `0.0037` n `6`; index avg `0.2108` n `23`; metal avg `-0.0083` n `18`; unknown avg `0.1974` n `421`
- 24h: commodity avg `0.6867` n `12`; crypto_alt avg `-1.1757` n `228`; crypto_major avg `-0.7591` n `8`; equity avg `0.8764` n `69`; fx avg `-0.0219` n `6`; index avg `0.3573` n `23`; metal avg `-0.1429` n `18`; unknown avg `0.4083` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2579`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
