# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T13:37:17.987050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0207` n `12`; crypto_alt avg `-0.4023` n `228`; crypto_major avg `-0.228` n `8`; equity avg `-0.0176` n `69`; fx avg `0.0` n `6`; index avg `-0.0157` n `23`; metal avg `-0.011` n `18`; unknown avg `0.7462` n `421`
- 1h: commodity avg `0.0343` n `12`; crypto_alt avg `-0.2051` n `228`; crypto_major avg `-0.0573` n `8`; equity avg `0.0744` n `69`; fx avg `-0.0129` n `6`; index avg `0.0338` n `23`; metal avg `-0.045` n `18`; unknown avg `-0.1218` n `421`
- 4h: commodity avg `0.2673` n `12`; crypto_alt avg `-0.2744` n `228`; crypto_major avg `0.1719` n `8`; equity avg `0.2599` n `69`; fx avg `-0.0043` n `6`; index avg `0.0601` n `23`; metal avg `-0.0568` n `18`; unknown avg `-0.0876` n `421`
- 24h: commodity avg `-0.1441` n `12`; crypto_alt avg `2.3476` n `228`; crypto_major avg `2.8101` n `8`; equity avg `1.7704` n `69`; fx avg `0.07` n `6`; index avg `0.1379` n `23`; metal avg `-0.045` n `18`; unknown avg `0.4895` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
