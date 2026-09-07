# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T16:52:32.799543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1969` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0097` n `12`; crypto_alt avg `0.0839` n `232`; crypto_major avg `0.0559` n `8`; equity avg `0.0146` n `134`; fx avg `0.0016` n `6`; index avg `0.0029` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.5843` n `796`
- 1h: commodity avg `-0.0059` n `12`; crypto_alt avg `0.7445` n `232`; crypto_major avg `0.4773` n `8`; equity avg `0.0902` n `134`; fx avg `-0.0007` n `6`; index avg `0.0097` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.977` n `788`
- 4h: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.9819` n `232`; crypto_major avg `-1.1581` n `8`; equity avg `0.0062` n `134`; fx avg `-0.0325` n `6`; index avg `0.0388` n `26`; metal avg `0.1441` n `20`; unknown avg `-0.5934` n `788`
- 24h: commodity avg `0.1206` n `12`; crypto_alt avg `0.1821` n `232`; crypto_major avg `-0.9643` n `8`; equity avg `0.4219` n `134`; fx avg `-0.1239` n `6`; index avg `0.0655` n `26`; metal avg `0.0267` n `20`; unknown avg `1.2261` n `681`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
