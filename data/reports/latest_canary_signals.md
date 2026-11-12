# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T08:52:32.595369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0417` n `13`; crypto_alt avg `0.0701` n `239`; crypto_major avg `0.0811` n `8`; equity avg `0.0786` n `161`; fx avg `-0.0171` n `6`; index avg `0.0088` n `27`; metal avg `-0.1075` n `20`; unknown avg `-0.0743` n `1262`
- 1h: commodity avg `0.0495` n `13`; crypto_alt avg `0.0608` n `239`; crypto_major avg `-0.0165` n `8`; equity avg `0.1848` n `161`; fx avg `-0.0009` n `6`; index avg `0.029` n `27`; metal avg `-0.1333` n `20`; unknown avg `17.521` n `1238`
- 4h: commodity avg `0.4142` n `13`; crypto_alt avg `-0.3774` n `239`; crypto_major avg `-0.3459` n `8`; equity avg `-0.243` n `161`; fx avg `0.0572` n `6`; index avg `-0.0449` n `27`; metal avg `-0.1786` n `20`; unknown avg `60.5636` n `1206`
- 24h: commodity avg `0.3951` n `13`; crypto_alt avg `-1.5465` n `239`; crypto_major avg `-0.65` n `8`; equity avg `-0.7627` n `161`; fx avg `-0.0679` n `6`; index avg `-0.0899` n `27`; metal avg `-0.7646` n `20`; unknown avg `17.7874` n `1125`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
