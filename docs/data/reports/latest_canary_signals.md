# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T02:22:30.802010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `12`; crypto_alt avg `0.0159` n `230`; crypto_major avg `0.0927` n `8`; equity avg `-0.0003` n `102`; fx avg `0.0455` n `6`; index avg `0.0131` n `25`; metal avg `-0.003` n `20`; unknown avg `0.0702` n `781`
- 1h: commodity avg `-0.0083` n `12`; crypto_alt avg `0.1057` n `230`; crypto_major avg `0.1291` n `8`; equity avg `0.0592` n `102`; fx avg `0.0331` n `6`; index avg `0.0512` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.0208` n `781`
- 4h: commodity avg `-0.1135` n `12`; crypto_alt avg `0.639` n `230`; crypto_major avg `0.2638` n `8`; equity avg `0.1747` n `102`; fx avg `-0.0157` n `6`; index avg `0.0485` n `25`; metal avg `-0.0211` n `20`; unknown avg `3.2921` n `781`
- 24h: commodity avg `0.906` n `12`; crypto_alt avg `0.2316` n `230`; crypto_major avg `-1.361` n `8`; equity avg `-1.8543` n `102`; fx avg `-0.0619` n `6`; index avg `-0.1475` n `25`; metal avg `-0.2111` n `20`; unknown avg `2.6831` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
