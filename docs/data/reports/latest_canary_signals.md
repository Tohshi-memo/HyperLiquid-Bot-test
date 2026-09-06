# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T08:52:29.229995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `0.0363` n `232`; crypto_major avg `0.0336` n `8`; equity avg `0.0101` n `134`; fx avg `0.003` n `6`; index avg `0.0029` n `26`; metal avg `0.0034` n `20`; unknown avg `0.6604` n `794`
- 1h: commodity avg `0.0204` n `12`; crypto_alt avg `-0.0969` n `232`; crypto_major avg `-0.0422` n `8`; equity avg `0.0319` n `134`; fx avg `-0.0219` n `6`; index avg `-0.0048` n `26`; metal avg `0.0108` n `20`; unknown avg `-0.0944` n `786`
- 4h: commodity avg `0.0309` n `12`; crypto_alt avg `-0.3051` n `232`; crypto_major avg `-0.2705` n `8`; equity avg `0.0628` n `134`; fx avg `0.014` n `6`; index avg `0.0108` n `26`; metal avg `-0.0103` n `20`; unknown avg `-0.0245` n `758`
- 24h: commodity avg `0.1643` n `12`; crypto_alt avg `1.6279` n `232`; crypto_major avg `1.7524` n `8`; equity avg `0.4344` n `134`; fx avg `-0.0178` n `6`; index avg `0.0885` n `26`; metal avg `0.0061` n `20`; unknown avg `493.2682` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
