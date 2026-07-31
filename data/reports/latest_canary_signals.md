# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T19:52:26.467774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `12`; crypto_alt avg `0.0427` n `230`; crypto_major avg `-0.0104` n `8`; equity avg `-0.0861` n `102`; fx avg `0.0052` n `6`; index avg `0.0317` n `25`; metal avg `0.0146` n `20`; unknown avg `-0.0813` n `780`
- 1h: commodity avg `0.0845` n `12`; crypto_alt avg `-0.2676` n `230`; crypto_major avg `-0.4017` n `8`; equity avg `-0.3812` n `102`; fx avg `0.0197` n `6`; index avg `-0.0148` n `25`; metal avg `-0.0061` n `20`; unknown avg `-0.2858` n `780`
- 4h: commodity avg `0.3031` n `12`; crypto_alt avg `0.1789` n `230`; crypto_major avg `-0.1011` n `8`; equity avg `0.5798` n `102`; fx avg `0.1026` n `6`; index avg `0.141` n `25`; metal avg `0.0997` n `20`; unknown avg `7.0954` n `780`
- 24h: commodity avg `0.2692` n `12`; crypto_alt avg `-0.667` n `230`; crypto_major avg `-2.2648` n `8`; equity avg `-0.0108` n `102`; fx avg `0.2235` n `6`; index avg `0.2511` n `25`; metal avg `-0.3505` n `20`; unknown avg `0.249` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
