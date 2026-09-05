# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T21:22:24.295154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0165` n `12`; crypto_alt avg `0.2818` n `232`; crypto_major avg `0.2037` n `8`; equity avg `0.0093` n `134`; fx avg `0.0019` n `6`; index avg `0.0059` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.0526` n `794`
- 1h: commodity avg `-0.0181` n `12`; crypto_alt avg `0.2745` n `232`; crypto_major avg `0.2403` n `8`; equity avg `0.0208` n `134`; fx avg `-0.0017` n `6`; index avg `0.0095` n `26`; metal avg `0.002` n `20`; unknown avg `18.4331` n `788`
- 4h: commodity avg `0.0546` n `12`; crypto_alt avg `0.416` n `232`; crypto_major avg `0.1589` n `8`; equity avg `0.0083` n `134`; fx avg `-0.0237` n `6`; index avg `0.0128` n `26`; metal avg `0.0097` n `20`; unknown avg `1.2242` n `770`
- 24h: commodity avg `0.0737` n `12`; crypto_alt avg `2.9925` n `232`; crypto_major avg `2.5419` n `8`; equity avg `0.1807` n `134`; fx avg `-0.0313` n `6`; index avg `0.0686` n `26`; metal avg `0.0655` n `20`; unknown avg `1281.0454` n `700`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
