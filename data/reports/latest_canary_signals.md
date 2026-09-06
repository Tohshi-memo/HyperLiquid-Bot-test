# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T20:32:21.101377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.0483` n `232`; crypto_major avg `0.1629` n `8`; equity avg `-0.0124` n `134`; fx avg `0.0023` n `6`; index avg `0.0015` n `26`; metal avg `0.0003` n `20`; unknown avg `146.0497` n `787`
- 1h: commodity avg `-0.0291` n `12`; crypto_alt avg `0.3158` n `232`; crypto_major avg `0.3038` n `8`; equity avg `0.0088` n `134`; fx avg `0.0005` n `6`; index avg `0.0115` n `26`; metal avg `0.0053` n `20`; unknown avg `0.0971` n `775`
- 4h: commodity avg `-0.0613` n `12`; crypto_alt avg `0.0943` n `232`; crypto_major avg `0.234` n `8`; equity avg `0.1978` n `134`; fx avg `0.0028` n `6`; index avg `0.0254` n `26`; metal avg `0.0361` n `20`; unknown avg `152.5035` n `755`
- 24h: commodity avg `0.0008` n `12`; crypto_alt avg `1.3564` n `232`; crypto_major avg `0.3813` n `8`; equity avg `0.3753` n `134`; fx avg `-0.0035` n `6`; index avg `0.0155` n `26`; metal avg `-0.0122` n `20`; unknown avg `100.751` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
