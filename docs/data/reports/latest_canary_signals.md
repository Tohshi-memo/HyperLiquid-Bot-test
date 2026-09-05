# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T11:07:27.866699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.059` n `232`; crypto_major avg `0.0198` n `8`; equity avg `-0.0084` n `134`; fx avg `0.0075` n `6`; index avg `0.0043` n `26`; metal avg `-0.0009` n `20`; unknown avg `-0.0163` n `788`
- 1h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.0755` n `232`; crypto_major avg `0.0209` n `8`; equity avg `-0.0401` n `134`; fx avg `0.0018` n `6`; index avg `0.0174` n `26`; metal avg `0.007` n `20`; unknown avg `0.3131` n `788`
- 4h: commodity avg `-0.0262` n `12`; crypto_alt avg `0.28` n `232`; crypto_major avg `0.5421` n `8`; equity avg `0.0292` n `134`; fx avg `-0.002` n `6`; index avg `0.0027` n `26`; metal avg `0.0002` n `20`; unknown avg `-0.0241` n `782`
- 24h: commodity avg `0.173` n `12`; crypto_alt avg `0.6349` n `232`; crypto_major avg `-1.2744` n `8`; equity avg `0.8666` n `134`; fx avg `-0.1131` n `6`; index avg `0.0669` n `26`; metal avg `-0.1286` n `20`; unknown avg `16.5045` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
