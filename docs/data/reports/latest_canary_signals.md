# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T23:37:30.561870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0161` n `12`; crypto_alt avg `0.0756` n `233`; crypto_major avg `0.0396` n `8`; equity avg `-0.0581` n `136`; fx avg `-0.0067` n `6`; index avg `-0.0237` n `27`; metal avg `0.0095` n `20`; unknown avg `0.1271` n `840`
- 1h: commodity avg `0.0079` n `12`; crypto_alt avg `-0.0232` n `233`; crypto_major avg `-0.1476` n `8`; equity avg `-0.1916` n `136`; fx avg `-0.0309` n `6`; index avg `-0.0136` n `27`; metal avg `0.0151` n `20`; unknown avg `8.5371` n `838`
- 4h: commodity avg `0.3168` n `12`; crypto_alt avg `-1.464` n `233`; crypto_major avg `-0.9251` n `8`; equity avg `-0.4212` n `136`; fx avg `0.0211` n `6`; index avg `-0.0504` n `27`; metal avg `-0.054` n `20`; unknown avg `16.4164` n `802`
- 24h: commodity avg `0.68` n `12`; crypto_alt avg `-1.5322` n `233`; crypto_major avg `-1.6694` n `8`; equity avg `-1.5784` n `130`; fx avg `0.042` n `6`; index avg `-0.3048` n `26`; metal avg `-0.1193` n `20`; unknown avg `2.6575` n `713`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
