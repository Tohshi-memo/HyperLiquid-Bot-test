# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T05:07:32.840855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6518` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0339` n `13`; crypto_alt avg `-0.0968` n `239`; crypto_major avg `0.0183` n `8`; equity avg `-0.2837` n `165`; fx avg `-0.0224` n `6`; index avg `-0.0227` n `27`; metal avg `-0.0575` n `20`; unknown avg `12.8516` n `1252`
- 1h: commodity avg `-0.0576` n `13`; crypto_alt avg `-0.4059` n `239`; crypto_major avg `-0.5075` n `8`; equity avg `-0.7269` n `165`; fx avg `-0.0277` n `6`; index avg `-0.0231` n `27`; metal avg `-0.1701` n `20`; unknown avg `-0.4157` n `1248`
- 4h: commodity avg `0.0459` n `13`; crypto_alt avg `-2.3231` n `239`; crypto_major avg `-1.7978` n `8`; equity avg `-1.5304` n `165`; fx avg `-0.0138` n `6`; index avg `-0.146` n `27`; metal avg `-0.6494` n `20`; unknown avg `0.4234` n `1242`
- 24h: commodity avg `-0.0804` n `13`; crypto_alt avg `-3.7341` n `239`; crypto_major avg `-3.0521` n `8`; equity avg `-6.2064` n `165`; fx avg `-0.0101` n `6`; index avg `-0.5244` n `27`; metal avg `-1.8651` n `20`; unknown avg `232.4194` n `1167`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
