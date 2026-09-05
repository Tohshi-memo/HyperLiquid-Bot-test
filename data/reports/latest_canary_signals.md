# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T17:52:24.000502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `0.0628` n `232`; crypto_major avg `0.1114` n `8`; equity avg `0.0031` n `134`; fx avg `-0.0053` n `6`; index avg `0.0014` n `26`; metal avg `0.0108` n `20`; unknown avg `-0.0316` n `794`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `0.3182` n `232`; crypto_major avg `0.4177` n `8`; equity avg `0.0679` n `134`; fx avg `-0.0194` n `6`; index avg `0.0028` n `26`; metal avg `0.0162` n `20`; unknown avg `0.0834` n `792`
- 4h: commodity avg `-0.0137` n `12`; crypto_alt avg `0.593` n `232`; crypto_major avg `1.1858` n `8`; equity avg `0.1571` n `134`; fx avg `-0.0191` n `6`; index avg `0.0307` n `26`; metal avg `0.0453` n `20`; unknown avg `-0.7189` n `782`
- 24h: commodity avg `0.0515` n `12`; crypto_alt avg `2.9335` n `232`; crypto_major avg `2.9072` n `8`; equity avg `0.5109` n `134`; fx avg `-0.0115` n `6`; index avg `0.0802` n `26`; metal avg `0.1637` n `20`; unknown avg `0.1897` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
