# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T18:52:24.776104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.1008` n `232`; crypto_major avg `-0.171` n `8`; equity avg `-0.0027` n `134`; fx avg `0.0011` n `6`; index avg `-0.0002` n `26`; metal avg `0.0017` n `20`; unknown avg `0.7997` n `793`
- 1h: commodity avg `-0.0086` n `12`; crypto_alt avg `0.1379` n `232`; crypto_major avg `0.05` n `8`; equity avg `0.0594` n `134`; fx avg `-0.0077` n `6`; index avg `0.0115` n `26`; metal avg `0.0036` n `20`; unknown avg `0.1211` n `785`
- 4h: commodity avg `-0.0281` n `12`; crypto_alt avg `0.4987` n `232`; crypto_major avg `0.0095` n `8`; equity avg `0.1779` n `134`; fx avg `-0.0307` n `6`; index avg `0.0364` n `26`; metal avg `-0.0083` n `20`; unknown avg `-0.521` n `770`
- 24h: commodity avg `0.0715` n `12`; crypto_alt avg `1.2306` n `232`; crypto_major avg `-0.2182` n `8`; equity avg `0.2989` n `134`; fx avg `-0.0247` n `6`; index avg `0.0201` n `26`; metal avg `-0.0415` n `20`; unknown avg `71.369` n `670`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
