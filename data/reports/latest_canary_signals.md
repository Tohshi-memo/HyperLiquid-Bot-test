# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T04:22:29.104503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0526` n `13`; crypto_alt avg `-0.0334` n `234`; crypto_major avg `0.0205` n `8`; equity avg `-0.0632` n `142`; fx avg `-0.0165` n `6`; index avg `-0.0199` n `26`; metal avg `-0.0193` n `20`; unknown avg `0.8219` n `974`
- 1h: commodity avg `-0.5912` n `13`; crypto_alt avg `0.4057` n `234`; crypto_major avg `0.318` n `8`; equity avg `0.2013` n `142`; fx avg `-0.0073` n `6`; index avg `0.0453` n `26`; metal avg `0.0435` n `20`; unknown avg `0.2241` n `966`
- 4h: commodity avg `-0.7591` n `13`; crypto_alt avg `0.8658` n `234`; crypto_major avg `0.1636` n `8`; equity avg `0.7186` n `142`; fx avg `0.0348` n `6`; index avg `0.1892` n `26`; metal avg `0.2159` n `20`; unknown avg `0.7985` n `950`
- 24h: commodity avg `-0.5608` n `13`; crypto_alt avg `1.1309` n `234`; crypto_major avg `0.825` n `8`; equity avg `0.5288` n `142`; fx avg `0.1793` n `6`; index avg `0.1771` n `26`; metal avg `-0.0429` n `20`; unknown avg `774.867` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
