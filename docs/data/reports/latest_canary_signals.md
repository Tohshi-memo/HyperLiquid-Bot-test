# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T01:22:30.319210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `13`; crypto_alt avg `0.071` n `237`; crypto_major avg `0.074` n `8`; equity avg `0.1724` n `151`; fx avg `-0.0024` n `6`; index avg `0.0601` n `26`; metal avg `0.0216` n `20`; unknown avg `0.1399` n `1199`
- 1h: commodity avg `0.0472` n `13`; crypto_alt avg `-0.1987` n `237`; crypto_major avg `-0.1589` n `8`; equity avg `-0.0659` n `151`; fx avg `0.026` n `6`; index avg `-0.0443` n `26`; metal avg `-0.1098` n `20`; unknown avg `0.6806` n `1197`
- 4h: commodity avg `0.1096` n `13`; crypto_alt avg `-0.1479` n `237`; crypto_major avg `-0.078` n `8`; equity avg `0.5515` n `151`; fx avg `-0.0009` n `6`; index avg `0.0248` n `26`; metal avg `-0.1341` n `20`; unknown avg `0.1629` n `1091`
- 24h: commodity avg `-0.0316` n `13`; crypto_alt avg `3.1331` n `237`; crypto_major avg `2.3024` n `8`; equity avg `2.7478` n `151`; fx avg `0.0496` n `6`; index avg `0.3638` n `26`; metal avg `0.1403` n `20`; unknown avg `212.3641` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
