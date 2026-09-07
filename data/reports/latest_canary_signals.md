# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T17:07:26.183174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1079` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0299` n `12`; crypto_alt avg `0.0758` n `232`; crypto_major avg `0.1346` n `8`; equity avg `0.1126` n `134`; fx avg `-0.0032` n `6`; index avg `0.026` n `26`; metal avg `0.0025` n `20`; unknown avg `0.8062` n `794`
- 1h: commodity avg `-0.0968` n `12`; crypto_alt avg `0.6137` n `232`; crypto_major avg `0.4647` n `8`; equity avg `0.2256` n `134`; fx avg `-0.0048` n `6`; index avg `0.0418` n `26`; metal avg `-0.0032` n `20`; unknown avg `1.1461` n `788`
- 4h: commodity avg `-0.1425` n `12`; crypto_alt avg `-1.0146` n `232`; crypto_major avg `-1.0561` n `8`; equity avg `0.0892` n `134`; fx avg `-0.0377` n `6`; index avg `0.0518` n `26`; metal avg `0.1504` n `20`; unknown avg `0.4141` n `788`
- 24h: commodity avg `0.0798` n `12`; crypto_alt avg `0.4888` n `232`; crypto_major avg `-0.7158` n `8`; equity avg `0.5087` n `134`; fx avg `-0.1088` n `6`; index avg `0.0868` n `26`; metal avg `0.0343` n `20`; unknown avg `2.6874` n `681`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
