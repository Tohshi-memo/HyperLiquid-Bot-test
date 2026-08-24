# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T00:52:25.910410+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.1509` n `231`; crypto_major avg `0.0045` n `8`; equity avg `0.1858` n `122`; fx avg `-0.0196` n `6`; index avg `0.0363` n `25`; metal avg `0.0718` n `20`; unknown avg `0.0` n `793`
- 1h: commodity avg `-0.0784` n `12`; crypto_alt avg `-0.9345` n `231`; crypto_major avg `-0.5274` n `8`; equity avg `-0.4805` n `122`; fx avg `-0.061` n `6`; index avg `-0.0521` n `25`; metal avg `-0.0325` n `20`; unknown avg `0.0645` n `793`
- 4h: commodity avg `-0.2229` n `12`; crypto_alt avg `-0.7299` n `231`; crypto_major avg `0.1113` n `8`; equity avg `-0.3462` n `122`; fx avg `-0.0651` n `6`; index avg `-0.0449` n `25`; metal avg `-0.0312` n `20`; unknown avg `0.3466` n `793`
- 24h: commodity avg `-0.3161` n `12`; crypto_alt avg `1.5923` n `231`; crypto_major avg `-0.281` n `8`; equity avg `0.2161` n `122`; fx avg `-0.1776` n `6`; index avg `0.0632` n `25`; metal avg `0.0733` n `20`; unknown avg `5.6917` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
