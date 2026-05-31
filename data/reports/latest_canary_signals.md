# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T23:07:18.980341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `0.1718` n `228`; crypto_major avg `0.0409` n `8`; equity avg `-0.0076` n `69`; fx avg `0.003` n `6`; index avg `0.1558` n `23`; metal avg `0.0408` n `18`; unknown avg `-0.1673` n `421`
- 1h: commodity avg `-0.3152` n `12`; crypto_alt avg `0.7788` n `228`; crypto_major avg `0.5736` n `8`; equity avg `0.0172` n `69`; fx avg `0.0074` n `6`; index avg `0.1537` n `23`; metal avg `0.4272` n `18`; unknown avg `0.8502` n `421`
- 4h: commodity avg `0.211` n `12`; crypto_alt avg `2.0537` n `228`; crypto_major avg `1.364` n `8`; equity avg `0.0811` n `69`; fx avg `-0.0099` n `6`; index avg `0.2732` n `23`; metal avg `0.1106` n `18`; unknown avg `1.7305` n `421`
- 24h: commodity avg `0.8119` n `12`; crypto_alt avg `1.2454` n `228`; crypto_major avg `0.7939` n `8`; equity avg `0.698` n `69`; fx avg `-0.019` n `6`; index avg `0.4407` n `23`; metal avg `0.004` n `18`; unknown avg `1.9617` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3406`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2447`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
