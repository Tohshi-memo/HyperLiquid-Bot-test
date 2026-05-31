# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T09:07:19.917265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0414` n `12`; crypto_alt avg `0.0805` n `228`; crypto_major avg `-0.0877` n `8`; equity avg `0.0156` n `69`; fx avg `0.0018` n `6`; index avg `0.0122` n `23`; metal avg `0.0006` n `18`; unknown avg `0.6238` n `421`
- 1h: commodity avg `0.0012` n `12`; crypto_alt avg `-0.0974` n `228`; crypto_major avg `-0.1762` n `8`; equity avg `-0.0402` n `69`; fx avg `0.0072` n `6`; index avg `-0.0943` n `23`; metal avg `-0.005` n `18`; unknown avg `0.6544` n `421`
- 4h: commodity avg `0.0925` n `12`; crypto_alt avg `-0.7084` n `228`; crypto_major avg `-0.7463` n `8`; equity avg `0.3864` n `69`; fx avg `0.0042` n `6`; index avg `-0.0693` n `23`; metal avg `0.0131` n `18`; unknown avg `0.6308` n `401`
- 24h: commodity avg `0.2522` n `12`; crypto_alt avg `0.2056` n `228`; crypto_major avg `1.5412` n `8`; equity avg `1.1724` n `69`; fx avg `0.024` n `6`; index avg `-0.0568` n `23`; metal avg `-0.0229` n `18`; unknown avg `2.3478` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
