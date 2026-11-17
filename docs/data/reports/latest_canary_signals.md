# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T04:52:27.354578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0307` n `13`; crypto_alt avg `0.1164` n `239`; crypto_major avg `0.1093` n `8`; equity avg `0.1507` n `162`; fx avg `0.0041` n `6`; index avg `0.0183` n `27`; metal avg `0.0479` n `20`; unknown avg `0.7725` n `1264`
- 1h: commodity avg `-0.0112` n `13`; crypto_alt avg `0.1115` n `239`; crypto_major avg `0.0055` n `8`; equity avg `-0.1982` n `162`; fx avg `-0.0215` n `6`; index avg `-0.0134` n `27`; metal avg `0.0436` n `20`; unknown avg `203.1009` n `1246`
- 4h: commodity avg `-0.1715` n `13`; crypto_alt avg `1.197` n `239`; crypto_major avg `1.0666` n `8`; equity avg `0.6701` n `162`; fx avg `-0.0021` n `6`; index avg `0.0311` n `27`; metal avg `0.2731` n `20`; unknown avg `0.3641` n `1242`
- 24h: commodity avg `-1.1534` n `13`; crypto_alt avg `0.7502` n `239`; crypto_major avg `1.4077` n `8`; equity avg `-2.249` n `162`; fx avg `-0.0554` n `6`; index avg `-0.2211` n `27`; metal avg `-0.0019` n `20`; unknown avg `560.1465` n `985`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
