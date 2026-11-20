# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T07:37:29.781215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0633` n `13`; crypto_alt avg `-0.0218` n `239`; crypto_major avg `-0.2917` n `8`; equity avg `-0.0827` n `165`; fx avg `-0.0198` n `6`; index avg `-0.0025` n `27`; metal avg `-0.0021` n `20`; unknown avg `0.6913` n `1262`
- 1h: commodity avg `-0.0722` n `13`; crypto_alt avg `-0.0718` n `239`; crypto_major avg `-0.2917` n `8`; equity avg `-0.2725` n `165`; fx avg `-0.0299` n `6`; index avg `-0.0119` n `27`; metal avg `-0.1051` n `20`; unknown avg `158.9004` n `1260`
- 4h: commodity avg `-0.125` n `13`; crypto_alt avg `-0.0108` n `239`; crypto_major avg `-0.2948` n `8`; equity avg `-0.7157` n `165`; fx avg `-0.0263` n `6`; index avg `-0.0634` n `27`; metal avg `0.1045` n `20`; unknown avg `0.3268` n `1220`
- 24h: commodity avg `-0.2215` n `13`; crypto_alt avg `-3.1558` n `239`; crypto_major avg `-2.8627` n `8`; equity avg `-7.1762` n `165`; fx avg `-0.0414` n `6`; index avg `-0.675` n `27`; metal avg `-1.6285` n `20`; unknown avg `7.4549` n `1169`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
