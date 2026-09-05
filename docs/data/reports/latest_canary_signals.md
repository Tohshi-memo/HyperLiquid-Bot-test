# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T10:07:25.332717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.0312` n `232`; crypto_major avg `-0.0015` n `8`; equity avg `0.0651` n `134`; fx avg `0.0059` n `6`; index avg `0.0019` n `26`; metal avg `-0.0056` n `20`; unknown avg `-0.0904` n `790`
- 1h: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.0108` n `232`; crypto_major avg `-0.0629` n `8`; equity avg `0.0768` n `134`; fx avg `-0.005` n `6`; index avg `0.0102` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.0216` n `788`
- 4h: commodity avg `-0.0122` n `12`; crypto_alt avg `0.6777` n `232`; crypto_major avg `0.9286` n `8`; equity avg `0.0802` n `134`; fx avg `-0.009` n `6`; index avg `-0.0061` n `26`; metal avg `-0.0098` n `20`; unknown avg `0.8845` n `774`
- 24h: commodity avg `0.093` n `12`; crypto_alt avg `0.6698` n `232`; crypto_major avg `-1.0954` n `8`; equity avg `0.8914` n `134`; fx avg `-0.1186` n `6`; index avg `0.0628` n `26`; metal avg `-0.108` n `20`; unknown avg `16.586` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
