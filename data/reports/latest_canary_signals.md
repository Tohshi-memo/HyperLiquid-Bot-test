# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T14:37:28.139710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1485` n `13`; crypto_alt avg `-0.8054` n `235`; crypto_major avg `-0.5574` n `8`; equity avg `-0.1737` n `144`; fx avg `0.0155` n `6`; index avg `-0.0268` n `26`; metal avg `-0.0782` n `20`; unknown avg `1.602` n `1053`
- 1h: commodity avg `0.1411` n `13`; crypto_alt avg `-0.7144` n `235`; crypto_major avg `-0.3212` n `8`; equity avg `0.0454` n `144`; fx avg `-0.0343` n `6`; index avg `0.0439` n `26`; metal avg `-0.0784` n `20`; unknown avg `0.1473` n `1015`
- 4h: commodity avg `-0.1881` n `13`; crypto_alt avg `-0.7828` n `235`; crypto_major avg `-0.43` n `8`; equity avg `0.016` n `144`; fx avg `-0.0764` n `6`; index avg `0.1298` n `26`; metal avg `-0.0808` n `20`; unknown avg `0.7551` n `1009`
- 24h: commodity avg `-0.247` n `13`; crypto_alt avg `-0.1546` n `235`; crypto_major avg `0.5994` n `8`; equity avg `0.0387` n `144`; fx avg `-0.1238` n `6`; index avg `0.0377` n `26`; metal avg `0.122` n `20`; unknown avg `-0.3848` n `828`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1995`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
