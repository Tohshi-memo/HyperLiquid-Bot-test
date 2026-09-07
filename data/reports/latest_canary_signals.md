# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T16:07:28.542153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1959` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0611` n `12`; crypto_alt avg `0.2061` n `232`; crypto_major avg `0.1472` n `8`; equity avg `-0.0224` n `134`; fx avg `0.0009` n `6`; index avg `-0.006` n `26`; metal avg `0.0004` n `20`; unknown avg `0.2615` n `794`
- 1h: commodity avg `-0.0584` n `12`; crypto_alt avg `-0.9377` n `232`; crypto_major avg `-0.5535` n `8`; equity avg `-0.1359` n `134`; fx avg `-0.0149` n `6`; index avg `0.0058` n `26`; metal avg `0.0098` n `20`; unknown avg `0.104` n `794`
- 4h: commodity avg `0.0637` n `12`; crypto_alt avg `-0.9497` n `232`; crypto_major avg `-1.1704` n `8`; equity avg `-0.1393` n `134`; fx avg `-0.0515` n `6`; index avg `0.0255` n `26`; metal avg `0.1953` n `20`; unknown avg `6613.8554` n `756`
- 24h: commodity avg `0.1982` n `12`; crypto_alt avg `0.0083` n `232`; crypto_major avg `-1.0863` n `8`; equity avg `0.323` n `134`; fx avg `-0.1118` n `6`; index avg `0.0476` n `26`; metal avg `0.019` n `20`; unknown avg `0.7338` n `681`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
