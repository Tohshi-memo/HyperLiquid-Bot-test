# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T17:07:25.503104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `-0.0686` n `230`; crypto_major avg `-0.0857` n `8`; equity avg `-0.026` n `96`; fx avg `0.0` n `6`; index avg `-0.0025` n `25`; metal avg `0.0006` n `20`; unknown avg `0.005` n `770`
- 1h: commodity avg `0.0068` n `12`; crypto_alt avg `0.0841` n `230`; crypto_major avg `0.2091` n `8`; equity avg `0.0232` n `96`; fx avg `-0.0103` n `6`; index avg `-0.013` n `25`; metal avg `-0.0029` n `20`; unknown avg `0.0531` n `770`
- 4h: commodity avg `-0.0071` n `12`; crypto_alt avg `0.1726` n `230`; crypto_major avg `0.2866` n `8`; equity avg `-0.1007` n `96`; fx avg `-0.0526` n `6`; index avg `-0.0263` n `25`; metal avg `-0.0454` n `20`; unknown avg `-0.0238` n `770`
- 24h: commodity avg `0.2773` n `12`; crypto_alt avg `-1.0491` n `230`; crypto_major avg `-0.1694` n `8`; equity avg `-1.6646` n `96`; fx avg `-0.1353` n `6`; index avg `-0.1881` n `25`; metal avg `-0.0489` n `20`; unknown avg `-0.0341` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
