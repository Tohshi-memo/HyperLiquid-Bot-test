# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T07:53:00.075978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `0.2872` n `232`; crypto_major avg `0.1689` n `8`; equity avg `0.0084` n `134`; fx avg `0.0006` n `6`; index avg `-0.0066` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.0493` n `794`
- 1h: commodity avg `-0.0174` n `12`; crypto_alt avg `-0.2444` n `232`; crypto_major avg `-0.2299` n `8`; equity avg `-0.0786` n `134`; fx avg `0.0364` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0235` n `20`; unknown avg `-0.0784` n `790`
- 4h: commodity avg `0.0047` n `12`; crypto_alt avg `-0.5499` n `232`; crypto_major avg `-0.4726` n `8`; equity avg `0.0008` n `134`; fx avg `0.0253` n `6`; index avg `0.009` n `26`; metal avg `-0.0267` n `20`; unknown avg `448.0761` n `744`
- 24h: commodity avg `0.1378` n `12`; crypto_alt avg `1.797` n `232`; crypto_major avg `2.0643` n `8`; equity avg `0.3969` n `134`; fx avg `-0.0096` n `6`; index avg `0.092` n `26`; metal avg `-0.0231` n `20`; unknown avg `493.3689` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
