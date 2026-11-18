# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T09:22:25.965638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0269` n `13`; crypto_alt avg `-0.0297` n `239`; crypto_major avg `-0.1428` n `8`; equity avg `-0.0854` n `163`; fx avg `0.0119` n `6`; index avg `0.0053` n `27`; metal avg `-0.0589` n `20`; unknown avg `10.243` n `1264`
- 1h: commodity avg `-0.0796` n `13`; crypto_alt avg `0.1886` n `239`; crypto_major avg `-0.0673` n `8`; equity avg `0.1968` n `163`; fx avg `-0.0058` n `6`; index avg `0.0399` n `27`; metal avg `-0.0143` n `20`; unknown avg `93.2682` n `1206`
- 4h: commodity avg `-0.1857` n `13`; crypto_alt avg `0.4641` n `239`; crypto_major avg `-0.0511` n `8`; equity avg `0.4434` n `163`; fx avg `-0.0974` n `6`; index avg `0.0829` n `27`; metal avg `-0.4665` n `20`; unknown avg `96.3871` n `1168`
- 24h: commodity avg `-0.1822` n `13`; crypto_alt avg `1.2131` n `239`; crypto_major avg `1.4584` n `8`; equity avg `2.2061` n `163`; fx avg `-0.1305` n `6`; index avg `0.2235` n `27`; metal avg `-1.0455` n `20`; unknown avg `5.8739` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
