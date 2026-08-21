# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T07:37:30.155496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0696` n `12`; crypto_alt avg `0.2569` n `230`; crypto_major avg `-0.1453` n `8`; equity avg `0.0457` n `121`; fx avg `-0.0117` n `6`; index avg `0.0105` n `25`; metal avg `-0.0164` n `20`; unknown avg `0.0537` n `793`
- 1h: commodity avg `0.069` n `12`; crypto_alt avg `0.8688` n `230`; crypto_major avg `0.375` n `8`; equity avg `0.3161` n `121`; fx avg `-0.0317` n `6`; index avg `0.0338` n `25`; metal avg `-0.0117` n `20`; unknown avg `0.1024` n `793`
- 4h: commodity avg `0.0683` n `12`; crypto_alt avg `1.9303` n `230`; crypto_major avg `1.2817` n `8`; equity avg `0.4966` n `121`; fx avg `-0.0102` n `6`; index avg `0.0506` n `25`; metal avg `0.1529` n `20`; unknown avg `0.0745` n `777`
- 24h: commodity avg `0.2539` n `12`; crypto_alt avg `7.1835` n `230`; crypto_major avg `7.3907` n `8`; equity avg `0.0458` n `121`; fx avg `-0.0351` n `6`; index avg `-0.0245` n `25`; metal avg `0.7497` n `20`; unknown avg `2.3884` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
