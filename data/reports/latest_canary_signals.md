# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T14:07:27.358924+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `12`; crypto_alt avg `0.0766` n `232`; crypto_major avg `0.2005` n `8`; equity avg `0.0172` n `134`; fx avg `0.0035` n `6`; index avg `-0.0022` n `26`; metal avg `0.0064` n `20`; unknown avg `0.1514` n `788`
- 1h: commodity avg `0.025` n `12`; crypto_alt avg `-0.3655` n `232`; crypto_major avg `-0.1063` n `8`; equity avg `-0.0265` n `134`; fx avg `0.0155` n `6`; index avg `-0.021` n `26`; metal avg `0.0087` n `20`; unknown avg `0.0828` n `736`
- 4h: commodity avg `0.0334` n `12`; crypto_alt avg `0.1211` n `232`; crypto_major avg `0.6362` n `8`; equity avg `-0.02` n `134`; fx avg `0.011` n `6`; index avg `0.0152` n `26`; metal avg `0.0074` n `20`; unknown avg `-0.0009` n `728`
- 24h: commodity avg `0.3996` n `12`; crypto_alt avg `2.2691` n `232`; crypto_major avg `1.4028` n `8`; equity avg `0.4119` n `134`; fx avg `0.0213` n `6`; index avg `0.0177` n `26`; metal avg `0.1087` n `20`; unknown avg `7.6561` n `660`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
