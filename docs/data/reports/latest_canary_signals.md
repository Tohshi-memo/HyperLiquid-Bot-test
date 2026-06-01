# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T23:07:19.100070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `5.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1737` n `12`; crypto_alt avg `0.1326` n `228`; crypto_major avg `0.0613` n `8`; equity avg `0.114` n `69`; fx avg `0.008` n `6`; index avg `0.0188` n `23`; metal avg `0.0345` n `18`; unknown avg `0.0614` n `422`
- 1h: commodity avg `-0.0686` n `12`; crypto_alt avg `0.8159` n `228`; crypto_major avg `0.9352` n `8`; equity avg `0.0414` n `69`; fx avg `0.0057` n `6`; index avg `0.0604` n `23`; metal avg `0.1111` n `18`; unknown avg `1.5076` n `422`
- 4h: commodity avg `-0.0502` n `12`; crypto_alt avg `0.0598` n `228`; crypto_major avg `0.4352` n `8`; equity avg `-0.4654` n `69`; fx avg `-0.0114` n `6`; index avg `-0.3446` n `23`; metal avg `-0.1282` n `18`; unknown avg `0.4985` n `422`
- 24h: commodity avg `0.1027` n `12`; crypto_alt avg `-0.1994` n `228`; crypto_major avg `-1.1376` n `8`; equity avg `-0.2206` n `69`; fx avg `0.0443` n `6`; index avg `-0.1114` n `23`; metal avg `-0.1315` n `18`; unknown avg `2.2737` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
