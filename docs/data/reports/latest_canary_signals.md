# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T23:52:29.658382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `13`; crypto_alt avg `0.0829` n `236`; crypto_major avg `0.0483` n `8`; equity avg `-0.1944` n `151`; fx avg `0.0027` n `6`; index avg `-0.023` n `26`; metal avg `-0.017` n `20`; unknown avg `1.7038` n `1136`
- 1h: commodity avg `0.0015` n `13`; crypto_alt avg `-0.2887` n `236`; crypto_major avg `-0.3384` n `8`; equity avg `-0.4455` n `151`; fx avg `-0.0167` n `6`; index avg `-0.0608` n `26`; metal avg `-0.0583` n `20`; unknown avg `0.0468` n `1134`
- 4h: commodity avg `-0.1015` n `13`; crypto_alt avg `-0.4438` n `236`; crypto_major avg `-0.4185` n `8`; equity avg `-0.5218` n `151`; fx avg `-0.0204` n `6`; index avg `-0.1131` n `26`; metal avg `-0.1092` n `20`; unknown avg `-0.3288` n `1028`
- 24h: commodity avg `-0.243` n `13`; crypto_alt avg `0.3938` n `236`; crypto_major avg `0.4623` n `8`; equity avg `1.2321` n `151`; fx avg `0.0992` n `6`; index avg `0.0823` n `26`; metal avg `0.4105` n `20`; unknown avg `24.7658` n `910`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0944`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0899`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0857`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0818`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0654`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0654`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0553`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0549`, n `666`, weak_sample_signal
