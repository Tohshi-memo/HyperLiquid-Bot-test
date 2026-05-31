# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T15:52:20.505819+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.3257` n `228`; crypto_major avg `-0.2373` n `8`; equity avg `0.0073` n `69`; fx avg `-0.0097` n `6`; index avg `-0.0266` n `23`; metal avg `-0.023` n `18`; unknown avg `-0.1971` n `421`
- 1h: commodity avg `0.0751` n `12`; crypto_alt avg `0.1161` n `228`; crypto_major avg `0.0187` n `8`; equity avg `0.0861` n `69`; fx avg `-0.0103` n `6`; index avg `0.0702` n `23`; metal avg `-0.05` n `18`; unknown avg `-0.1856` n `421`
- 4h: commodity avg `0.1162` n `12`; crypto_alt avg `-0.8698` n `228`; crypto_major avg `-0.3655` n `8`; equity avg `0.0786` n `69`; fx avg `-0.0079` n `6`; index avg `0.1288` n `23`; metal avg `-0.0494` n `18`; unknown avg `-0.5617` n `421`
- 24h: commodity avg `0.2306` n `12`; crypto_alt avg `-0.875` n `228`; crypto_major avg `0.1544` n `8`; equity avg `0.8155` n `69`; fx avg `-0.0361` n `6`; index avg `-0.1108` n `23`; metal avg `-0.122` n `18`; unknown avg `0.1174` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
