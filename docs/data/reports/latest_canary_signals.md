# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T10:37:30.200210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0369` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.0091` n `233`; crypto_major avg `-0.0279` n `8`; equity avg `-0.0363` n `136`; fx avg `0.0018` n `6`; index avg `-0.0118` n `27`; metal avg `-0.003` n `20`; unknown avg `-0.0285` n `838`
- 1h: commodity avg `-0.0046` n `12`; crypto_alt avg `0.0292` n `233`; crypto_major avg `-0.0345` n `8`; equity avg `-0.079` n `136`; fx avg `0.0012` n `6`; index avg `-0.0137` n `27`; metal avg `-0.0088` n `20`; unknown avg `-0.0251` n `836`
- 4h: commodity avg `0.0014` n `12`; crypto_alt avg `-0.9037` n `233`; crypto_major avg `-1.1864` n `8`; equity avg `-0.9318` n `136`; fx avg `0.0124` n `6`; index avg `-0.1495` n `26`; metal avg `-0.0608` n `20`; unknown avg `0.122` n `830`
- 24h: commodity avg `0.1167` n `12`; crypto_alt avg `-0.5494` n `233`; crypto_major avg `-1.8069` n `8`; equity avg `-1.6868` n `136`; fx avg `-0.001` n `6`; index avg `-0.2761` n `26`; metal avg `-0.0377` n `20`; unknown avg `-0.1355` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
