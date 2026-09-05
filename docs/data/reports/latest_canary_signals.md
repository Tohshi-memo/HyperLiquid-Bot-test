# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T14:22:27.143460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `-0.0164` n `232`; crypto_major avg `0.0018` n `8`; equity avg `0.0076` n `134`; fx avg `0.001` n `6`; index avg `-0.008` n `26`; metal avg `-0.0025` n `20`; unknown avg `-0.1217` n `794`
- 1h: commodity avg `0.04` n `12`; crypto_alt avg `-0.3294` n `232`; crypto_major avg `-0.2292` n `8`; equity avg `-0.0172` n `134`; fx avg `0.005` n `6`; index avg `-0.0254` n `26`; metal avg `0.0035` n `20`; unknown avg `0.0599` n `736`
- 4h: commodity avg `0.0502` n `12`; crypto_alt avg `0.09` n `232`; crypto_major avg `0.6808` n `8`; equity avg `0.0294` n `134`; fx avg `0.0132` n `6`; index avg `-0.0126` n `26`; metal avg `-0.0015` n `20`; unknown avg `-0.0356` n `728`
- 24h: commodity avg `0.2884` n `12`; crypto_alt avg `2.535` n `232`; crypto_major avg `1.7323` n `8`; equity avg `0.5569` n `134`; fx avg `0.0182` n `6`; index avg `0.0281` n `26`; metal avg `0.0369` n `20`; unknown avg `0.2075` n `656`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
