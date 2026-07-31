# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T22:52:34.830208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `-0.0544` n `230`; crypto_major avg `-0.0553` n `8`; equity avg `-0.0218` n `102`; fx avg `-0.0039` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.0618` n `781`
- 1h: commodity avg `-0.171` n `12`; crypto_alt avg `-0.0349` n `230`; crypto_major avg `0.0075` n `8`; equity avg `-0.0561` n `102`; fx avg `0.0111` n `6`; index avg `0.0325` n `25`; metal avg `0.0094` n `20`; unknown avg `1.3531` n `781`
- 4h: commodity avg `0.6293` n `12`; crypto_alt avg `-0.3964` n `230`; crypto_major avg `-0.5096` n `8`; equity avg `-1.0594` n `102`; fx avg `-0.0807` n `6`; index avg `-0.1369` n `25`; metal avg `-0.0789` n `20`; unknown avg `1.7699` n `780`
- 24h: commodity avg `0.779` n `12`; crypto_alt avg `-0.7757` n `230`; crypto_major avg `-2.474` n `8`; equity avg `-1.6891` n `102`; fx avg `0.1008` n `6`; index avg `0.0022` n `25`; metal avg `-0.4377` n `20`; unknown avg `2.5255` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
