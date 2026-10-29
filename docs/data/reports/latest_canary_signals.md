# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T10:22:32.279774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `13`; crypto_alt avg `-0.0551` n `238`; crypto_major avg `-0.1511` n `8`; equity avg `-0.1471` n `155`; fx avg `0.0157` n `6`; index avg `-0.0208` n `27`; metal avg `0.0388` n `20`; unknown avg `0.0505` n `1212`
- 1h: commodity avg `-0.0837` n `13`; crypto_alt avg `-0.12` n `238`; crypto_major avg `-0.3029` n `8`; equity avg `-0.1103` n `155`; fx avg `0.0438` n `6`; index avg `0.0165` n `27`; metal avg `0.012` n `20`; unknown avg `-0.1333` n `1192`
- 4h: commodity avg `-0.0333` n `13`; crypto_alt avg `0.041` n `238`; crypto_major avg `-0.126` n `8`; equity avg `-0.1226` n `155`; fx avg `0.0461` n `6`; index avg `0.0287` n `27`; metal avg `-0.072` n `20`; unknown avg `-0.17` n `1166`
- 24h: commodity avg `-0.2125` n `13`; crypto_alt avg `-2.7276` n `238`; crypto_major avg `-2.3536` n `8`; equity avg `-1.5546` n `155`; fx avg `0.0619` n `6`; index avg `0.0018` n `27`; metal avg `-0.3501` n `20`; unknown avg `27.2841` n `1000`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
