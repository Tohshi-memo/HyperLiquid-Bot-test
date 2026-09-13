# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T22:22:29.743866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.192` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0567` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `-0.7645` n `233`; crypto_major avg `-0.5968` n `8`; equity avg `-0.1619` n `136`; fx avg `0.004` n `6`; index avg `-0.018` n `27`; metal avg `-0.0655` n `20`; unknown avg `0.0238` n `840`
- 1h: commodity avg `0.37` n `12`; crypto_alt avg `-1.7743` n `233`; crypto_major avg `-1.2916` n `8`; equity avg `-0.3813` n `136`; fx avg `0.0085` n `6`; index avg `-0.0996` n `27`; metal avg `-0.126` n `20`; unknown avg `4.0151` n `838`
- 4h: commodity avg `0.3926` n `12`; crypto_alt avg `-1.8439` n `233`; crypto_major avg `-1.1475` n `8`; equity avg `-0.3635` n `136`; fx avg `0.0419` n `6`; index avg `-0.0908` n `27`; metal avg `-0.1372` n `20`; unknown avg `8.1734` n `794`
- 24h: commodity avg `0.6382` n `12`; crypto_alt avg `-1.5854` n `233`; crypto_major avg `-1.7434` n `8`; equity avg `-1.4467` n `136`; fx avg `0.052` n `6`; index avg `-0.3232` n `26`; metal avg `-0.1908` n `20`; unknown avg `2.2524` n `716`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
