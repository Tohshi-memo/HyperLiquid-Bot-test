# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T02:37:30.898307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `0.0378` n `237`; crypto_major avg `0.0113` n `8`; equity avg `-0.1192` n `151`; fx avg `0.0229` n `6`; index avg `-0.0488` n `26`; metal avg `-0.0304` n `20`; unknown avg `0.4564` n `1198`
- 1h: commodity avg `-0.0924` n `13`; crypto_alt avg `0.1673` n `237`; crypto_major avg `0.0595` n `8`; equity avg `0.4192` n `151`; fx avg `0.0124` n `6`; index avg `0.0274` n `26`; metal avg `0.1629` n `20`; unknown avg `1.9574` n `1196`
- 4h: commodity avg `0.0642` n `13`; crypto_alt avg `-0.4484` n `237`; crypto_major avg `-0.4553` n `8`; equity avg `-0.6035` n `151`; fx avg `-0.0038` n `6`; index avg `-0.1416` n `26`; metal avg `-0.0022` n `20`; unknown avg `-0.0827` n `1188`
- 24h: commodity avg `0.168` n `13`; crypto_alt avg `-0.2348` n `237`; crypto_major avg `-0.547` n `8`; equity avg `-0.6039` n `151`; fx avg `0.027` n `6`; index avg `-0.0891` n `26`; metal avg `-0.2456` n `20`; unknown avg `5.1737` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
