# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T16:00:28.935145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `0.0318` n `232`; crypto_major avg `0.0148` n `8`; equity avg `0.0053` n `129`; fx avg `0.0116` n `6`; index avg `-0.0025` n `26`; metal avg `-0.0013` n `20`; unknown avg `-0.0837` n `788`
- 1h: commodity avg `0.0347` n `12`; crypto_alt avg `-0.1803` n `232`; crypto_major avg `0.0229` n `8`; equity avg `0.0157` n `129`; fx avg `-0.0006` n `6`; index avg `-0.0067` n `26`; metal avg `0.01` n `20`; unknown avg `-0.3095` n `788`
- 4h: commodity avg `0.0634` n `12`; crypto_alt avg `0.0744` n `232`; crypto_major avg `0.7403` n `8`; equity avg `0.0562` n `129`; fx avg `0.0204` n `6`; index avg `0.005` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.2213` n `725`
- 24h: commodity avg `0.082` n `12`; crypto_alt avg `2.3126` n `232`; crypto_major avg `1.865` n `8`; equity avg `0.3967` n `129`; fx avg `0.0031` n `6`; index avg `0.0284` n `26`; metal avg `0.0097` n `20`; unknown avg `0.068` n `655`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
