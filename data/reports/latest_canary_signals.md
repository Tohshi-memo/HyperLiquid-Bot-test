# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T23:22:24.193813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `-0.0064` n `230`; crypto_major avg `0.02` n `8`; equity avg `0.0144` n `92`; fx avg `-0.0015` n `6`; index avg `0.0065` n `25`; metal avg `0.0011` n `20`; unknown avg `-0.0915` n `766`
- 1h: commodity avg `-0.0165` n `12`; crypto_alt avg `0.0373` n `230`; crypto_major avg `0.0056` n `8`; equity avg `0.1379` n `92`; fx avg `-0.025` n `6`; index avg `0.0386` n `25`; metal avg `-0.0122` n `20`; unknown avg `-0.0047` n `766`
- 4h: commodity avg `0.0421` n `12`; crypto_alt avg `0.119` n `230`; crypto_major avg `0.0309` n `8`; equity avg `0.161` n `92`; fx avg `-0.0169` n `6`; index avg `0.0405` n `25`; metal avg `-0.0394` n `20`; unknown avg `-0.253` n `766`
- 24h: commodity avg `0.1111` n `12`; crypto_alt avg `2.3353` n `230`; crypto_major avg `3.6663` n `8`; equity avg `1.8802` n `92`; fx avg `-0.0106` n `6`; index avg `0.5078` n `25`; metal avg `0.5693` n `20`; unknown avg `0.1846` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
