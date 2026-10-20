# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T23:22:33.023745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `13`; crypto_alt avg `-0.0065` n `237`; crypto_major avg `-0.0539` n `8`; equity avg `-0.1129` n `151`; fx avg `-0.0076` n `6`; index avg `-0.0147` n `26`; metal avg `-0.0408` n `20`; unknown avg `0.142` n `1183`
- 1h: commodity avg `0.0407` n `13`; crypto_alt avg `-0.3622` n `237`; crypto_major avg `-0.3698` n `8`; equity avg `-0.3326` n `151`; fx avg `-0.0211` n `6`; index avg `-0.0528` n `26`; metal avg `-0.095` n `20`; unknown avg `0.4212` n `1125`
- 4h: commodity avg `0.0192` n `13`; crypto_alt avg `0.7976` n `237`; crypto_major avg `0.7507` n `8`; equity avg `1.3192` n `151`; fx avg `-0.0228` n `6`; index avg `0.1621` n `26`; metal avg `0.0071` n `20`; unknown avg `0.2382` n `1033`
- 24h: commodity avg `0.0091` n `13`; crypto_alt avg `2.244` n `237`; crypto_major avg `1.4754` n `8`; equity avg `1.1964` n `151`; fx avg `0.02` n `6`; index avg `0.1141` n `26`; metal avg `0.0547` n `20`; unknown avg `211.3272` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
