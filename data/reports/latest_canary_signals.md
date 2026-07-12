# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T09:37:29.343090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `0.2152` n `230`; crypto_major avg `0.271` n `8`; equity avg `0.0002` n `92`; fx avg `-0.0039` n `6`; index avg `-0.0057` n `25`; metal avg `-0.002` n `20`; unknown avg `0.161` n `765`
- 1h: commodity avg `0.0664` n `12`; crypto_alt avg `-0.1271` n `230`; crypto_major avg `-0.0553` n `8`; equity avg `-0.0083` n `92`; fx avg `-0.0006` n `6`; index avg `-0.0174` n `25`; metal avg `-0.0038` n `20`; unknown avg `4.3202` n `765`
- 4h: commodity avg `0.1189` n `12`; crypto_alt avg `-0.2393` n `230`; crypto_major avg `-0.0213` n `8`; equity avg `-0.116` n `92`; fx avg `-0.0011` n `6`; index avg `-0.0119` n `25`; metal avg `-0.0252` n `20`; unknown avg `2.041` n `747`
- 24h: commodity avg `0.5281` n `12`; crypto_alt avg `-0.9151` n `230`; crypto_major avg `-0.7047` n `8`; equity avg `-0.2334` n `92`; fx avg `-0.0002` n `6`; index avg `-0.1305` n `25`; metal avg `-0.1091` n `20`; unknown avg `0.0451` n `747`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
