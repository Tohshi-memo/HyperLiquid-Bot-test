# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T12:22:23.488643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4182` n `12`; crypto_alt avg `0.0931` n `228`; crypto_major avg `0.066` n `8`; equity avg `-0.0721` n `69`; fx avg `0.006` n `6`; index avg `-0.0866` n `23`; metal avg `-0.2675` n `18`; unknown avg `-0.1088` n `422`
- 1h: commodity avg `-0.554` n `12`; crypto_alt avg `-0.4317` n `228`; crypto_major avg `-0.3757` n `8`; equity avg `-0.1493` n `69`; fx avg `0.0037` n `6`; index avg `-0.1064` n `23`; metal avg `-0.2307` n `18`; unknown avg `1.263` n `418`
- 4h: commodity avg `-0.959` n `12`; crypto_alt avg `-0.0111` n `228`; crypto_major avg `0.2259` n `8`; equity avg `-0.258` n `69`; fx avg `-0.0074` n `6`; index avg `-0.1421` n `23`; metal avg `0.167` n `18`; unknown avg `1.8607` n `416`
- 24h: commodity avg `0.2582` n `12`; crypto_alt avg `-0.844` n `228`; crypto_major avg `-0.7909` n `8`; equity avg `-0.5114` n `69`; fx avg `-0.0019` n `6`; index avg `0.4073` n `23`; metal avg `0.0605` n `18`; unknown avg `3.0423` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.289`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.208`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
