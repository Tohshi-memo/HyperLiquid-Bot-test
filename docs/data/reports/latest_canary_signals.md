# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T08:52:18.775832+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1147` n `12`; crypto_alt avg `-0.0295` n `228`; crypto_major avg `-0.0455` n `8`; equity avg `0.0951` n `69`; fx avg `0.0073` n `6`; index avg `0.0589` n `23`; metal avg `0.0935` n `18`; unknown avg `-0.1821` n `422`
- 1h: commodity avg `-0.0826` n `12`; crypto_alt avg `-0.0837` n `228`; crypto_major avg `-0.0472` n `8`; equity avg `-0.1424` n `69`; fx avg `-0.0079` n `6`; index avg `-0.5309` n `23`; metal avg `0.1255` n `18`; unknown avg `0.0628` n `422`
- 4h: commodity avg `0.4767` n `12`; crypto_alt avg `-1.4727` n `228`; crypto_major avg `-1.0817` n `8`; equity avg `-0.4993` n `69`; fx avg `-0.0506` n `6`; index avg `-0.3658` n `23`; metal avg `-0.1046` n `18`; unknown avg `-0.1084` n `412`
- 24h: commodity avg `1.2394` n `12`; crypto_alt avg `-0.5591` n `228`; crypto_major avg `-1.2557` n `8`; equity avg `-0.324` n `69`; fx avg `-0.0163` n `6`; index avg `0.4787` n `23`; metal avg `0.0324` n `18`; unknown avg `1.2446` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2879`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
