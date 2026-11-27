# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T10:37:22.873377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0232` n `13`; crypto_alt avg `0.0547` n `239`; crypto_major avg `0.075` n `8`; equity avg `0.1017` n `168`; fx avg `0.0103` n `6`; index avg `0.0151` n `27`; metal avg `0.0178` n `20`; unknown avg `0.1988` n `1261`
- 1h: commodity avg `-0.0168` n `13`; crypto_alt avg `-0.2816` n `239`; crypto_major avg `-0.2139` n `8`; equity avg `-0.2357` n `168`; fx avg `0.0236` n `6`; index avg `0.0034` n `27`; metal avg `-0.1097` n `20`; unknown avg `159.962` n `1253`
- 4h: commodity avg `-0.2316` n `13`; crypto_alt avg `-0.1602` n `239`; crypto_major avg `0.1715` n `8`; equity avg `-0.09` n `168`; fx avg `-0.0448` n `6`; index avg `-0.029` n `27`; metal avg `0.0518` n `20`; unknown avg `179.692` n `1115`
- 24h: commodity avg `0.3161` n `13`; crypto_alt avg `1.865` n `239`; crypto_major avg `2.915` n `8`; equity avg `4.1542` n `168`; fx avg `-0.1005` n `6`; index avg `0.3302` n `27`; metal avg `1.2909` n `20`; unknown avg `71.917` n `1021`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
