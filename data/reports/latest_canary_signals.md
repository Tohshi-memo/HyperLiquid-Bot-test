# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T10:52:30.734547+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1211` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0141` n `12`; crypto_alt avg `-0.2815` n `233`; crypto_major avg `-0.2186` n `8`; equity avg `-0.0619` n `136`; fx avg `0.0025` n `6`; index avg `-0.0113` n `27`; metal avg `-0.0113` n `20`; unknown avg `-0.0155` n `838`
- 1h: commodity avg `0.0214` n `12`; crypto_alt avg `-0.287` n `233`; crypto_major avg `-0.3117` n `8`; equity avg `-0.1568` n `136`; fx avg `0.0044` n `6`; index avg `-0.0328` n `27`; metal avg `-0.0233` n `20`; unknown avg `-0.0414` n `836`
- 4h: commodity avg `0.0128` n `12`; crypto_alt avg `-1.0768` n `233`; crypto_major avg `-1.2796` n `8`; equity avg `-0.9657` n `136`; fx avg `0.0143` n `6`; index avg `-0.1585` n `26`; metal avg `-0.0712` n `20`; unknown avg `0.6716` n `830`
- 24h: commodity avg `0.1357` n `12`; crypto_alt avg `-0.7741` n `233`; crypto_major avg `-2.0056` n `8`; equity avg `-1.7295` n `136`; fx avg `0.0033` n `6`; index avg `-0.2851` n `26`; metal avg `-0.0459` n `20`; unknown avg `-0.1895` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
