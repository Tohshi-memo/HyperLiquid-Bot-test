# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T22:07:32.678112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0442` n `12`; crypto_alt avg `-0.0689` n `228`; crypto_major avg `-0.1341` n `8`; equity avg `-0.0093` n `88`; fx avg `-0.0012` n `6`; index avg `0.0018` n `23`; metal avg `-0.0115` n `20`; unknown avg `0.29` n `765`
- 1h: commodity avg `-0.025` n `12`; crypto_alt avg `0.2654` n `228`; crypto_major avg `0.3124` n `8`; equity avg `0.0324` n `88`; fx avg `0.0246` n `6`; index avg `-0.0315` n `23`; metal avg `0.0188` n `20`; unknown avg `0.375` n `765`
- 4h: commodity avg `-0.1204` n `12`; crypto_alt avg `-0.4869` n `228`; crypto_major avg `0.1202` n `8`; equity avg `0.463` n `88`; fx avg `0.024` n `6`; index avg `0.0446` n `23`; metal avg `-0.0136` n `20`; unknown avg `0.1358` n `765`
- 24h: commodity avg `-0.1962` n `12`; crypto_alt avg `1.4627` n `228`; crypto_major avg `2.7335` n `8`; equity avg `1.5995` n `88`; fx avg `0.2137` n `6`; index avg `0.0647` n `23`; metal avg `-0.5` n `20`; unknown avg `1.7324` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
