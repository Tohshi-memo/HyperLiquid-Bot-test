# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T21:02:08.551072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `0.0147` n `230`; crypto_major avg `0.0667` n `8`; equity avg `0.0149` n `92`; fx avg `-0.0009` n `6`; index avg `-0.0012` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.0645` n `765`
- 1h: commodity avg `0.0341` n `12`; crypto_alt avg `0.0375` n `230`; crypto_major avg `0.0874` n `8`; equity avg `0.0393` n `92`; fx avg `0.0024` n `6`; index avg `-0.0093` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.0275` n `765`
- 4h: commodity avg `0.0588` n `12`; crypto_alt avg `0.3338` n `230`; crypto_major avg `0.3527` n `8`; equity avg `0.159` n `92`; fx avg `0.0175` n `6`; index avg `-0.0071` n `25`; metal avg `0.0027` n `20`; unknown avg `-0.0082` n `765`
- 24h: commodity avg `0.0023` n `12`; crypto_alt avg `1.1865` n `229`; crypto_major avg `0.979` n `8`; equity avg `0.3972` n `92`; fx avg `0.0078` n `6`; index avg `0.0141` n `25`; metal avg `-0.044` n `20`; unknown avg `2.3098` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
