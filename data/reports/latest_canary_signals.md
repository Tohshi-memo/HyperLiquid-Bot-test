# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T08:09:38.279526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `13`; crypto_alt avg `0.1547` n `239`; crypto_major avg `0.1975` n `8`; equity avg `0.3065` n `166`; fx avg `0.0045` n `6`; index avg `0.0439` n `27`; metal avg `-0.1736` n `20`; unknown avg `0.1294` n `1238`
- 1h: commodity avg `0.002` n `13`; crypto_alt avg `0.187` n `239`; crypto_major avg `0.1216` n `8`; equity avg `0.4723` n `166`; fx avg `0.0238` n `6`; index avg `0.0603` n `27`; metal avg `-0.1927` n `20`; unknown avg `0.8263` n `1240`
- 4h: commodity avg `-0.2857` n `13`; crypto_alt avg `0.9164` n `239`; crypto_major avg `0.5294` n `8`; equity avg `0.7377` n `166`; fx avg `0.0002` n `6`; index avg `0.0511` n `27`; metal avg `0.0638` n `20`; unknown avg `0.0578` n `1212`
- 24h: commodity avg `-0.6028` n `13`; crypto_alt avg `2.4992` n `239`; crypto_major avg `3.1541` n `8`; equity avg `2.8995` n `166`; fx avg `0.2424` n `6`; index avg `0.1943` n `27`; metal avg `0.4088` n `20`; unknown avg `348.1422` n `995`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
