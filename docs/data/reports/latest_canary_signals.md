# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T06:07:33.368915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0531` n `12`; crypto_alt avg `-0.3741` n `234`; crypto_major avg `-0.3293` n `8`; equity avg `-0.1916` n `140`; fx avg `0.012` n `6`; index avg `-0.0238` n `26`; metal avg `-0.1013` n `20`; unknown avg `-0.0838` n `916`
- 1h: commodity avg `0.0647` n `12`; crypto_alt avg `-0.1306` n `234`; crypto_major avg `-0.0467` n `8`; equity avg `-0.2745` n `140`; fx avg `0.0344` n `6`; index avg `-0.023` n `26`; metal avg `-0.1799` n `20`; unknown avg `8.2018` n `916`
- 4h: commodity avg `0.151` n `12`; crypto_alt avg `-0.3448` n `234`; crypto_major avg `-0.3343` n `8`; equity avg `-0.8133` n `140`; fx avg `-0.0042` n `6`; index avg `-0.1023` n `26`; metal avg `-0.2163` n `20`; unknown avg `0.312` n `910`
- 24h: commodity avg `-0.1189` n `12`; crypto_alt avg `2.7498` n `234`; crypto_major avg `3.9569` n `8`; equity avg `1.5474` n `140`; fx avg `-0.2398` n `6`; index avg `0.3612` n `26`; metal avg `-0.1674` n `20`; unknown avg `7.0738` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
