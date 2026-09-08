# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T08:07:31.282732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `11`; crypto_alt avg `-0.0347` n `232`; crypto_major avg `0.0998` n `8`; equity avg `-0.2889` n `123`; fx avg `0.0171` n `5`; index avg `-0.0275` n `20`; metal avg `0.0112` n `18`; unknown avg `0.818` n `793`
- 1h: commodity avg `0.108` n `12`; crypto_alt avg `0.0383` n `232`; crypto_major avg `0.0862` n `8`; equity avg `-0.5122` n `134`; fx avg `-0.0368` n `6`; index avg `-0.1013` n `26`; metal avg `-0.1157` n `20`; unknown avg `0.5106` n `795`
- 4h: commodity avg `0.3159` n `12`; crypto_alt avg `-0.1506` n `232`; crypto_major avg `-0.0866` n `8`; equity avg `-1.3536` n `134`; fx avg `0.075` n `6`; index avg `-0.3195` n `26`; metal avg `-0.3064` n `20`; unknown avg `1.6048` n `747`
- 24h: commodity avg `0.5814` n `12`; crypto_alt avg `0.7639` n `232`; crypto_major avg `-0.7769` n `8`; equity avg `-0.6009` n `134`; fx avg `-0.1629` n `6`; index avg `-0.1671` n `26`; metal avg `-0.0178` n `20`; unknown avg `7509.503` n `666`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
