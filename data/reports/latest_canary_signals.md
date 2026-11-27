# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T14:07:40.184224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1025` n `13`; crypto_alt avg `-0.0836` n `239`; crypto_major avg `-0.1693` n `8`; equity avg `-0.1884` n `168`; fx avg `-0.0086` n `6`; index avg `-0.0216` n `27`; metal avg `-0.0842` n `20`; unknown avg `0.5685` n `1250`
- 1h: commodity avg `-0.0367` n `13`; crypto_alt avg `0.1341` n `239`; crypto_major avg `0.1467` n `8`; equity avg `-0.2247` n `168`; fx avg `-0.0117` n `6`; index avg `-0.0492` n `27`; metal avg `-0.2769` n `20`; unknown avg `0.5947` n `1258`
- 4h: commodity avg `-0.3266` n `13`; crypto_alt avg `0.0145` n `239`; crypto_major avg `-0.1133` n `8`; equity avg `-0.2938` n `168`; fx avg `-0.0073` n `6`; index avg `-0.0081` n `27`; metal avg `-0.4084` n `20`; unknown avg `25.3062` n `1247`
- 24h: commodity avg `-0.2383` n `13`; crypto_alt avg `1.8073` n `239`; crypto_major avg `2.4752` n `8`; equity avg `3.1901` n `168`; fx avg `-0.1233` n `6`; index avg `0.253` n `27`; metal avg `0.8072` n `20`; unknown avg `232.0183` n `1025`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
