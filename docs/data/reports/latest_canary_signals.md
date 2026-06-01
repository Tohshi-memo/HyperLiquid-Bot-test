# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T09:52:21.235092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `0.1683` n `228`; crypto_major avg `0.1217` n `8`; equity avg `-0.0838` n `69`; fx avg `0.013` n `6`; index avg `-0.0159` n `23`; metal avg `-0.0664` n `18`; unknown avg `-0.3263` n `422`
- 1h: commodity avg `-0.0544` n `12`; crypto_alt avg `0.255` n `228`; crypto_major avg `0.7265` n `8`; equity avg `0.0004` n `69`; fx avg `0.0039` n `6`; index avg `-0.055` n `23`; metal avg `0.0061` n `18`; unknown avg `-0.0911` n `422`
- 4h: commodity avg `0.2771` n `12`; crypto_alt avg `-1.2326` n `228`; crypto_major avg `-0.3548` n `8`; equity avg `-0.5299` n `69`; fx avg `0.0509` n `6`; index avg `-0.1028` n `23`; metal avg `-0.3756` n `18`; unknown avg `-0.2588` n `412`
- 24h: commodity avg `1.2398` n `12`; crypto_alt avg `-0.5806` n `228`; crypto_major avg `-0.5313` n `8`; equity avg `-0.3103` n `69`; fx avg `-0.0112` n `6`; index avg `0.4475` n `23`; metal avg `0.0617` n `18`; unknown avg `1.2985` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2879`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
