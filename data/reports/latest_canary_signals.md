# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T10:07:21.564907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `-0.2993` n `228`; crypto_major avg `-0.1391` n `8`; equity avg `-0.0258` n `69`; fx avg `-0.0045` n `6`; index avg `-0.0009` n `23`; metal avg `-0.0106` n `18`; unknown avg `1.1348` n `421`
- 1h: commodity avg `-0.0294` n `12`; crypto_alt avg `-0.1091` n `228`; crypto_major avg `-0.0705` n `8`; equity avg `-0.047` n `69`; fx avg `-0.0074` n `6`; index avg `-0.0386` n `23`; metal avg `-0.0324` n `18`; unknown avg `-0.2437` n `421`
- 4h: commodity avg `0.0828` n `12`; crypto_alt avg `-0.4576` n `228`; crypto_major avg `-0.6301` n `8`; equity avg `0.277` n `69`; fx avg `-0.0032` n `6`; index avg `-0.1122` n `23`; metal avg `-0.0312` n `18`; unknown avg `0.5446` n `421`
- 24h: commodity avg `0.215` n `12`; crypto_alt avg `-0.0073` n `228`; crypto_major avg `1.3384` n `8`; equity avg `1.1147` n `69`; fx avg `0.0147` n `6`; index avg `-0.0757` n `23`; metal avg `-0.0902` n `18`; unknown avg `2.1532` n `401`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
