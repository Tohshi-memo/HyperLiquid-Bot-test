# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T04:37:28.455574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0276` n `13`; crypto_alt avg `-0.2161` n `239`; crypto_major avg `-0.1357` n `8`; equity avg `-0.1653` n `161`; fx avg `0.0206` n `6`; index avg `-0.0313` n `27`; metal avg `-0.0201` n `20`; unknown avg `0.0458` n `1258`
- 1h: commodity avg `-0.0547` n `13`; crypto_alt avg `-0.2872` n `239`; crypto_major avg `-0.1291` n `8`; equity avg `-0.103` n `161`; fx avg `-0.0118` n `6`; index avg `0.0004` n `27`; metal avg `-0.0433` n `20`; unknown avg `-0.1325` n `1240`
- 4h: commodity avg `-0.1238` n `13`; crypto_alt avg `-0.7407` n `239`; crypto_major avg `-0.5621` n `8`; equity avg `-0.3236` n `161`; fx avg `-0.0881` n `6`; index avg `-0.0252` n `27`; metal avg `-0.0168` n `20`; unknown avg `19.6675` n `1238`
- 24h: commodity avg `0.0367` n `13`; crypto_alt avg `-2.1696` n `239`; crypto_major avg `-0.6497` n `8`; equity avg `0.2282` n `161`; fx avg `-0.2223` n `6`; index avg `-0.0036` n `27`; metal avg `-0.4261` n `20`; unknown avg `-0.2865` n `1129`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
