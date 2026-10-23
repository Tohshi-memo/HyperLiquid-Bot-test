# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T21:07:29.552442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0264` n `13`; crypto_alt avg `0.0902` n `237`; crypto_major avg `0.0007` n `8`; equity avg `0.011` n `152`; fx avg `0.0065` n `6`; index avg `-0.002` n `26`; metal avg `0.015` n `20`; unknown avg `0.0504` n `1222`
- 1h: commodity avg `-0.0387` n `13`; crypto_alt avg `0.2194` n `237`; crypto_major avg `0.2578` n `8`; equity avg `0.1498` n `152`; fx avg `0.0003` n `6`; index avg `0.0316` n `26`; metal avg `0.0029` n `20`; unknown avg `0.4121` n `1172`
- 4h: commodity avg `0.1376` n `13`; crypto_alt avg `-0.845` n `237`; crypto_major avg `-0.5891` n `8`; equity avg `-0.3813` n `152`; fx avg `-0.0177` n `6`; index avg `-0.0039` n `26`; metal avg `-0.0599` n `20`; unknown avg `0.4352` n `1143`
- 24h: commodity avg `0.4372` n `13`; crypto_alt avg `0.5683` n `237`; crypto_major avg `0.5051` n `8`; equity avg `1.4205` n `152`; fx avg `-0.0745` n `6`; index avg `0.1169` n `26`; metal avg `-0.1445` n `20`; unknown avg `0.2579` n `1022`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1995`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
