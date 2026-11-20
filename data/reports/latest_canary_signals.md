# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T08:37:24.948534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1173` n `13`; crypto_alt avg `0.1445` n `239`; crypto_major avg `0.1474` n `8`; equity avg `-0.0506` n `165`; fx avg `-0.001` n `6`; index avg `-0.0079` n `27`; metal avg `0.1572` n `20`; unknown avg `0.3673` n `1260`
- 1h: commodity avg `-0.2519` n `13`; crypto_alt avg `0.4895` n `239`; crypto_major avg `0.5956` n `8`; equity avg `0.6826` n `165`; fx avg `-0.0109` n `6`; index avg `0.101` n `27`; metal avg `0.4142` n `20`; unknown avg `4.1314` n `1204`
- 4h: commodity avg `-0.419` n `13`; crypto_alt avg `1.3278` n `239`; crypto_major avg `1.249` n `8`; equity avg `0.1785` n `165`; fx avg `-0.0381` n `6`; index avg `0.0864` n `27`; metal avg `0.6275` n `20`; unknown avg `0.4706` n `1184`
- 24h: commodity avg `-0.4138` n `13`; crypto_alt avg `-2.7657` n `239`; crypto_major avg `-2.2688` n `8`; equity avg `-6.7665` n `165`; fx avg `-0.0744` n `6`; index avg `-0.6109` n `27`; metal avg `-1.2584` n `20`; unknown avg `6.7306` n `1163`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
