# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T04:07:36.668475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1194` n `13`; crypto_alt avg `-0.1577` n `239`; crypto_major avg `-0.249` n `8`; equity avg `-0.1288` n `162`; fx avg `-0.0207` n `6`; index avg `-0.0213` n `27`; metal avg `-0.0338` n `20`; unknown avg `2.0095` n `1253`
- 1h: commodity avg `0.2048` n `13`; crypto_alt avg `-0.5078` n `239`; crypto_major avg `-0.5563` n `8`; equity avg `-0.5393` n `162`; fx avg `-0.0208` n `6`; index avg `-0.0579` n `27`; metal avg `-0.015` n `20`; unknown avg `0.065` n `1253`
- 4h: commodity avg `0.0453` n `13`; crypto_alt avg `-0.8176` n `239`; crypto_major avg `-1.0636` n `8`; equity avg `-1.5929` n `162`; fx avg `-0.0593` n `6`; index avg `-0.2604` n `27`; metal avg `-0.4147` n `20`; unknown avg `0.8218` n `1239`
- 24h: commodity avg `-0.2717` n `13`; crypto_alt avg `-0.1143` n `239`; crypto_major avg `0.009` n `8`; equity avg `-0.0905` n `162`; fx avg `-0.0444` n `6`; index avg `-0.0124` n `27`; metal avg `0.13` n `20`; unknown avg `0.6089` n `1125`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
