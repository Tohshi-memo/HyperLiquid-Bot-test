# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T06:07:28.795204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0921` n `12`; crypto_alt avg `-0.1839` n `228`; crypto_major avg `-0.1047` n `8`; equity avg `-0.1114` n `74`; fx avg `-0.005` n `6`; index avg `-0.0715` n `23`; metal avg `-0.4799` n `18`; unknown avg `-0.0216` n `540`
- 1h: commodity avg `-0.1493` n `12`; crypto_alt avg `-0.4205` n `228`; crypto_major avg `0.0714` n `8`; equity avg `-0.1181` n `74`; fx avg `0.0307` n `6`; index avg `-0.0811` n `23`; metal avg `-0.0982` n `18`; unknown avg `-0.1963` n `540`
- 4h: commodity avg `-0.328` n `12`; crypto_alt avg `0.69` n `228`; crypto_major avg `0.5036` n `8`; equity avg `0.1244` n `74`; fx avg `-0.017` n `6`; index avg `0.1112` n `23`; metal avg `-0.3645` n `18`; unknown avg `2.8308` n `540`
- 24h: commodity avg `1.5785` n `12`; crypto_alt avg `1.1642` n `228`; crypto_major avg `0.9285` n `8`; equity avg `-0.5344` n `74`; fx avg `0.0201` n `6`; index avg `-0.6332` n `23`; metal avg `-1.3328` n `18`; unknown avg `2.7989` n `537`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
