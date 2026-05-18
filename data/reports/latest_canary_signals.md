# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T12:22:18.827873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3119` n `12`; crypto_alt avg `0.1384` n `228`; crypto_major avg `0.0765` n `8`; equity avg `-0.0782` n `66`; fx avg `0.0151` n `5`; index avg `-0.0395` n `23`; metal avg `-0.045` n `18`; unknown avg `0.105` n `383`
- 1h: commodity avg `-0.2146` n `12`; crypto_alt avg `1.1941` n `228`; crypto_major avg `1.0636` n `8`; equity avg `0.5027` n `66`; fx avg `-0.0086` n `5`; index avg `0.219` n `23`; metal avg `0.5372` n `18`; unknown avg `0.4768` n `383`
- 4h: commodity avg `-0.1121` n `12`; crypto_alt avg `0.8657` n `228`; crypto_major avg `0.7349` n `8`; equity avg `0.026` n `66`; fx avg `0.055` n `5`; index avg `-0.0227` n `23`; metal avg `0.3111` n `18`; unknown avg `-0.0083` n `383`
- 24h: commodity avg `0.6063` n `12`; crypto_alt avg `-1.998` n `228`; crypto_major avg `-0.9997` n `8`; equity avg `0.2984` n `65`; fx avg `0.0996` n `5`; index avg `0.1559` n `23`; metal avg `0.4192` n `18`; unknown avg `-0.4363` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
