# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T03:52:35.365169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `0.1678` n `232`; crypto_major avg `0.0617` n `8`; equity avg `0.0007` n `134`; fx avg `0.0075` n `6`; index avg `0.0056` n `26`; metal avg `0.0013` n `20`; unknown avg `0.8857` n `778`
- 1h: commodity avg `0.0009` n `12`; crypto_alt avg `0.3632` n `232`; crypto_major avg `0.5602` n `8`; equity avg `0.0468` n `134`; fx avg `0.0135` n `6`; index avg `-0.0059` n `26`; metal avg `0.015` n `20`; unknown avg `7.99` n `776`
- 4h: commodity avg `0.0089` n `12`; crypto_alt avg `1.0103` n `232`; crypto_major avg `0.954` n `8`; equity avg `0.1163` n `134`; fx avg `0.0137` n `6`; index avg `0.0058` n `26`; metal avg `-0.0025` n `20`; unknown avg `2.0285` n `770`
- 24h: commodity avg `0.1273` n `12`; crypto_alt avg `3.2506` n `232`; crypto_major avg `3.1611` n `8`; equity avg `0.5082` n `134`; fx avg `-0.0563` n `6`; index avg `0.097` n `26`; metal avg `0.026` n `20`; unknown avg `1.1472` n `692`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
