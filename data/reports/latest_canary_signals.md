# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T14:07:25.944641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `0.0857` n `230`; crypto_major avg `-0.0308` n `8`; equity avg `0.0263` n `122`; fx avg `-0.006` n `6`; index avg `0.0021` n `25`; metal avg `-0.0042` n `20`; unknown avg `0.0588` n `794`
- 1h: commodity avg `0.0019` n `12`; crypto_alt avg `1.1239` n `230`; crypto_major avg `0.4993` n `8`; equity avg `0.0623` n `122`; fx avg `-0.006` n `6`; index avg `0.0012` n `25`; metal avg `-0.0104` n `20`; unknown avg `0.4986` n `794`
- 4h: commodity avg `0.0139` n `12`; crypto_alt avg `2.911` n `230`; crypto_major avg `1.4846` n `8`; equity avg `0.2312` n `122`; fx avg `-0.0187` n `6`; index avg `0.0139` n `25`; metal avg `0.0479` n `20`; unknown avg `2.8867` n `793`
- 24h: commodity avg `0.0547` n `12`; crypto_alt avg `2.4287` n `230`; crypto_major avg `1.855` n `8`; equity avg `0.5371` n `122`; fx avg `0.0553` n `6`; index avg `0.0495` n `25`; metal avg `0.0572` n `20`; unknown avg `6.9899` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
