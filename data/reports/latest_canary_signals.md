# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T22:37:32.547141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `12`; crypto_alt avg `-0.0536` n `230`; crypto_major avg `-0.0452` n `8`; equity avg `0.0575` n `102`; fx avg `-0.0144` n `6`; index avg `0.0187` n `25`; metal avg `0.0081` n `20`; unknown avg `-0.0384` n `781`
- 1h: commodity avg `-0.1364` n `12`; crypto_alt avg `0.0015` n `230`; crypto_major avg `-0.0142` n `8`; equity avg `-0.1313` n `102`; fx avg `0.0118` n `6`; index avg `0.0118` n `25`; metal avg `0.0257` n `20`; unknown avg `2.5177` n `781`
- 4h: commodity avg `0.6149` n `12`; crypto_alt avg `-0.2312` n `230`; crypto_major avg `-0.185` n `8`; equity avg `-0.9591` n `102`; fx avg `-0.0684` n `6`; index avg `-0.1205` n `25`; metal avg `-0.0825` n `20`; unknown avg `1.8782` n `780`
- 24h: commodity avg `0.7199` n `12`; crypto_alt avg `-0.8348` n `230`; crypto_major avg `-2.5069` n `8`; equity avg `-1.6707` n `102`; fx avg `0.1031` n `6`; index avg `-0.0029` n `25`; metal avg `-0.422` n `20`; unknown avg `2.5279` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
