# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T06:22:26.190316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0201` n `13`; crypto_alt avg `0.2194` n `239`; crypto_major avg `0.1471` n `8`; equity avg `0.1603` n `164`; fx avg `-0.0159` n `6`; index avg `0.0173` n `27`; metal avg `-0.0101` n `20`; unknown avg `0.1401` n `1260`
- 1h: commodity avg `0.0132` n `13`; crypto_alt avg `0.2507` n `239`; crypto_major avg `0.3759` n `8`; equity avg `0.5038` n `164`; fx avg `-0.0154` n `6`; index avg `0.0785` n `27`; metal avg `0.073` n `20`; unknown avg `40112.5935` n `1232`
- 4h: commodity avg `-0.016` n `13`; crypto_alt avg `0.5609` n `239`; crypto_major avg `1.2871` n `8`; equity avg `0.5608` n `164`; fx avg `-0.0047` n `6`; index avg `0.1234` n `27`; metal avg `-0.0238` n `20`; unknown avg `48234.6109` n `1211`
- 24h: commodity avg `0.2119` n `13`; crypto_alt avg `-0.0986` n `239`; crypto_major avg `-0.7242` n `8`; equity avg `-0.0605` n `164`; fx avg `-0.1261` n `6`; index avg `0.1072` n `27`; metal avg `-0.3868` n `20`; unknown avg `51776.6091` n `1107`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
