# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T11:07:27.828934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0252` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0541` n `12`; crypto_alt avg `0.1422` n `233`; crypto_major avg `0.1061` n `8`; equity avg `0.0408` n `136`; fx avg `0.0018` n `6`; index avg `0.0021` n `27`; metal avg `0.0022` n `20`; unknown avg `0.0185` n `836`
- 1h: commodity avg `0.0617` n `12`; crypto_alt avg `-0.2204` n `233`; crypto_major avg `-0.2094` n `8`; equity avg `-0.1173` n `136`; fx avg `0.005` n `6`; index avg `-0.0325` n `27`; metal avg `-0.0162` n `20`; unknown avg `0.0091` n `836`
- 4h: commodity avg `0.0677` n `12`; crypto_alt avg `-0.923` n `233`; crypto_major avg `-1.1737` n `8`; equity avg `-0.8759` n `136`; fx avg `0.014` n `6`; index avg `-0.1485` n `26`; metal avg `-0.0627` n `20`; unknown avg `0.576` n `830`
- 24h: commodity avg `0.1963` n `12`; crypto_alt avg `-0.693` n `233`; crypto_major avg `-1.9344` n `8`; equity avg `-1.7131` n `136`; fx avg `0.0097` n `6`; index avg `-0.2824` n `26`; metal avg `-0.0425` n `20`; unknown avg `-0.0963` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
