# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T19:07:28.023055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0251` n `12`; crypto_alt avg `0.2989` n `230`; crypto_major avg `0.3364` n `8`; equity avg `0.6133` n `102`; fx avg `-0.0023` n `6`; index avg `0.1068` n `25`; metal avg `0.0569` n `20`; unknown avg `0.3181` n `774`
- 1h: commodity avg `-0.01` n `12`; crypto_alt avg `-0.102` n `230`; crypto_major avg `-0.0928` n `8`; equity avg `0.5244` n `102`; fx avg `0.0079` n `6`; index avg `0.1075` n `25`; metal avg `0.0058` n `20`; unknown avg `0.1016` n `774`
- 4h: commodity avg `-0.2039` n `12`; crypto_alt avg `0.2081` n `230`; crypto_major avg `0.3347` n `8`; equity avg `0.642` n `102`; fx avg `-0.036` n `6`; index avg `0.0254` n `25`; metal avg `0.0083` n `20`; unknown avg `-0.2126` n `774`
- 24h: commodity avg `-0.9417` n `12`; crypto_alt avg `-1.0893` n `230`; crypto_major avg `-0.3429` n `8`; equity avg `-1.1791` n `102`; fx avg `0.0012` n `6`; index avg `-0.3436` n `25`; metal avg `0.1721` n `20`; unknown avg `-0.3595` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1804`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
