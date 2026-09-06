# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T18:37:24.593455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `0.1089` n `232`; crypto_major avg `0.1071` n `8`; equity avg `0.022` n `134`; fx avg `-0.0106` n `6`; index avg `0.0` n `26`; metal avg `-0.0068` n `20`; unknown avg `1.5821` n `793`
- 1h: commodity avg `-0.0394` n `12`; crypto_alt avg `0.1791` n `232`; crypto_major avg `0.2201` n `8`; equity avg `0.0947` n `134`; fx avg `-0.0094` n `6`; index avg `0.0111` n `26`; metal avg `0.0082` n `20`; unknown avg `1.1474` n `785`
- 4h: commodity avg `-0.0494` n `12`; crypto_alt avg `0.8325` n `232`; crypto_major avg `0.359` n `8`; equity avg `0.1622` n `134`; fx avg `-0.021` n `6`; index avg `0.0181` n `26`; metal avg `0.013` n `20`; unknown avg `-0.3393` n `770`
- 24h: commodity avg `0.048` n `12`; crypto_alt avg `1.2375` n `232`; crypto_major avg `-0.165` n `8`; equity avg `0.297` n `134`; fx avg `-0.0225` n `6`; index avg `0.0359` n `26`; metal avg `-0.0427` n `20`; unknown avg `91.9701` n `670`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
