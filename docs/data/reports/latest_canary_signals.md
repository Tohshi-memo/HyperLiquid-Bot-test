# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T23:22:21.569576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `5.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.021` n `12`; crypto_alt avg `0.0454` n `228`; crypto_major avg `0.1625` n `8`; equity avg `0.0045` n `69`; fx avg `-0.0062` n `6`; index avg `0.0233` n `23`; metal avg `0.0527` n `18`; unknown avg `0.0613` n `422`
- 1h: commodity avg `-0.0294` n `12`; crypto_alt avg `0.6319` n `228`; crypto_major avg `0.7011` n `8`; equity avg `0.0264` n `69`; fx avg `0.0066` n `6`; index avg `0.0282` n `23`; metal avg `0.1509` n `18`; unknown avg `0.4444` n `422`
- 4h: commodity avg `-0.1092` n `12`; crypto_alt avg `0.123` n `228`; crypto_major avg `0.5654` n `8`; equity avg `-0.4239` n `69`; fx avg `-0.0241` n `6`; index avg `-0.317` n `23`; metal avg `-0.0406` n `18`; unknown avg `0.7102` n `422`
- 24h: commodity avg `0.0566` n `12`; crypto_alt avg `0.2256` n `228`; crypto_major avg `-0.6421` n `8`; equity avg `-0.1707` n `69`; fx avg `0.0399` n `6`; index avg `0.2647` n `23`; metal avg `-0.1535` n `18`; unknown avg `2.3745` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
