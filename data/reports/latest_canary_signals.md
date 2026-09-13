# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T11:22:30.304363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0749` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0821` n `12`; crypto_alt avg `-0.0217` n `233`; crypto_major avg `-0.0175` n `8`; equity avg `-0.0214` n `136`; fx avg `0.0021` n `6`; index avg `0.004` n `27`; metal avg `-0.001` n `20`; unknown avg `0.0301` n `838`
- 1h: commodity avg `0.1496` n `12`; crypto_alt avg `-0.1535` n `233`; crypto_major avg `-0.1582` n `8`; equity avg `-0.0788` n `136`; fx avg `0.0081` n `6`; index avg `-0.017` n `27`; metal avg `-0.013` n `20`; unknown avg `0.0823` n `836`
- 4h: commodity avg `0.1449` n `12`; crypto_alt avg `-0.9925` n `233`; crypto_major avg `-1.213` n `8`; equity avg `-0.876` n `136`; fx avg `0.0179` n `6`; index avg `-0.1381` n `27`; metal avg `-0.0606` n `20`; unknown avg `0.6922` n `830`
- 24h: commodity avg `0.2624` n `12`; crypto_alt avg `-0.6118` n `233`; crypto_major avg `-1.902` n `8`; equity avg `-1.7331` n `136`; fx avg `0.0111` n `6`; index avg `-0.2782` n `26`; metal avg `-0.0409` n `20`; unknown avg `-0.1078` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
