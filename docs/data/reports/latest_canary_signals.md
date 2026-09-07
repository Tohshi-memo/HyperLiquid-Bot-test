# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T11:07:25.193224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1393` n `12`; crypto_alt avg `-0.1612` n `232`; crypto_major avg `-0.1375` n `8`; equity avg `-0.0844` n `134`; fx avg `0.0267` n `6`; index avg `-0.0322` n `26`; metal avg `-0.0255` n `20`; unknown avg `0.8055` n `794`
- 1h: commodity avg `0.2373` n `12`; crypto_alt avg `0.1262` n `232`; crypto_major avg `0.0039` n `8`; equity avg `-0.0213` n `134`; fx avg `0.0447` n `6`; index avg `-0.0404` n `26`; metal avg `-0.035` n `20`; unknown avg `-0.1675` n `794`
- 4h: commodity avg `0.1457` n `12`; crypto_alt avg `0.2207` n `232`; crypto_major avg `-0.2269` n `8`; equity avg `-0.1025` n `134`; fx avg `-0.0537` n `6`; index avg `-0.068` n `26`; metal avg `0.0029` n `20`; unknown avg `1.5374` n `784`
- 24h: commodity avg `0.1623` n `12`; crypto_alt avg `-0.0142` n `232`; crypto_major avg `-0.8566` n `8`; equity avg `0.2143` n `134`; fx avg `-0.0856` n `6`; index avg `-0.0165` n `26`; metal avg `-0.1404` n `20`; unknown avg `75.7129` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
