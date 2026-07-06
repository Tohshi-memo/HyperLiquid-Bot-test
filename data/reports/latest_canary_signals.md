# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T13:07:29.202766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7075` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0308` n `12`; crypto_alt avg `-0.3301` n `229`; crypto_major avg `-0.46` n `8`; equity avg `-0.1336` n `88`; fx avg `0.0068` n `6`; index avg `-0.0019` n `25`; metal avg `0.0495` n `20`; unknown avg `-0.1073` n `765`
- 1h: commodity avg `-0.1943` n `12`; crypto_alt avg `0.2096` n `229`; crypto_major avg `-0.4396` n `8`; equity avg `-0.1773` n `88`; fx avg `0.0188` n `6`; index avg `-0.012` n `25`; metal avg `-0.2847` n `20`; unknown avg `-0.0497` n `765`
- 4h: commodity avg `-0.0626` n `12`; crypto_alt avg `-1.1382` n `229`; crypto_major avg `-1.6963` n `8`; equity avg `-0.3831` n `88`; fx avg `0.0128` n `6`; index avg `0.0112` n `25`; metal avg `-0.2489` n `20`; unknown avg `-0.0292` n `765`
- 24h: commodity avg `-0.2159` n `12`; crypto_alt avg `-1.652` n `229`; crypto_major avg `-1.6424` n `8`; equity avg `-1.0054` n `88`; fx avg `0.1403` n `6`; index avg `-0.0081` n `25`; metal avg `-0.4609` n `20`; unknown avg `0.6144` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
