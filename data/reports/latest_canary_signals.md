# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T02:37:27.692471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `12`; crypto_alt avg `-0.0767` n `230`; crypto_major avg `-0.0626` n `8`; equity avg `-0.0052` n `102`; fx avg `-0.0331` n `6`; index avg `-0.0073` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0856` n `781`
- 1h: commodity avg `0.0233` n `12`; crypto_alt avg `-0.072` n `230`; crypto_major avg `0.078` n `8`; equity avg `0.105` n `102`; fx avg `-0.0003` n `6`; index avg `0.026` n `25`; metal avg `0.0028` n `20`; unknown avg `0.1893` n `781`
- 4h: commodity avg `-0.0861` n `12`; crypto_alt avg `0.5828` n `230`; crypto_major avg `0.2238` n `8`; equity avg `0.092` n `102`; fx avg `-0.0363` n `6`; index avg `0.0208` n `25`; metal avg `-0.0305` n `20`; unknown avg `0.1198` n `781`
- 24h: commodity avg `0.9299` n `12`; crypto_alt avg `0.3091` n `230`; crypto_major avg `-1.2825` n `8`; equity avg `-1.7383` n `102`; fx avg `-0.0976` n `6`; index avg `-0.1256` n `25`; metal avg `-0.2064` n `20`; unknown avg `4.9407` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
