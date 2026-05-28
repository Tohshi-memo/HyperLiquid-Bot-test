# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T23:52:20.193452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `-0.0939` n `228`; crypto_major avg `-0.204` n `8`; equity avg `-0.0305` n `69`; fx avg `0.0104` n `6`; index avg `-0.0107` n `23`; metal avg `-0.0576` n `18`; unknown avg `-0.0085` n `417`
- 1h: commodity avg `-0.0794` n `12`; crypto_alt avg `0.0692` n `228`; crypto_major avg `-0.0673` n `8`; equity avg `0.1193` n `69`; fx avg `0.0224` n `6`; index avg `0.0332` n `23`; metal avg `-0.0003` n `18`; unknown avg `-0.1076` n `417`
- 4h: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.1639` n `228`; crypto_major avg `-0.1913` n `8`; equity avg `0.5345` n `69`; fx avg `0.018` n `6`; index avg `-0.1281` n `23`; metal avg `0.005` n `18`; unknown avg `-0.2072` n `417`
- 24h: commodity avg `0.5746` n `12`; crypto_alt avg `-1.9468` n `228`; crypto_major avg `0.2368` n `8`; equity avg `2.7156` n `69`; fx avg `0.0115` n `6`; index avg `0.9393` n `23`; metal avg `0.7055` n `18`; unknown avg `0.0535` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1823`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
