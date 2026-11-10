# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T02:07:26.355193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0435` n `13`; crypto_alt avg `-0.0617` n `239`; crypto_major avg `-0.2719` n `8`; equity avg `0.0073` n `160`; fx avg `0.006` n `6`; index avg `0.0036` n `27`; metal avg `0.0022` n `20`; unknown avg `0.3303` n `1257`
- 1h: commodity avg `-0.0799` n `13`; crypto_alt avg `-0.1681` n `239`; crypto_major avg `-0.3786` n `8`; equity avg `0.1222` n `160`; fx avg `0.0202` n `6`; index avg `0.0343` n `27`; metal avg `-0.0831` n `20`; unknown avg `-0.1289` n `1253`
- 4h: commodity avg `-0.0692` n `13`; crypto_alt avg `-0.3604` n `239`; crypto_major avg `-0.1074` n `8`; equity avg `-0.3839` n `160`; fx avg `0.0692` n `6`; index avg `-0.0934` n `27`; metal avg `-0.0782` n `20`; unknown avg `-0.0443` n `1249`
- 24h: commodity avg `-0.4698` n `13`; crypto_alt avg `0.312` n `239`; crypto_major avg `-0.8057` n `8`; equity avg `3.5286` n `160`; fx avg `0.0211` n `6`; index avg `0.3705` n `27`; metal avg `0.0035` n `20`; unknown avg `184.192` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
