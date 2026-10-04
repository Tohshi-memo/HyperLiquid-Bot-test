# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T06:22:31.650043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `-0.0276` n `235`; crypto_major avg `0.0409` n `8`; equity avg `0.0041` n `143`; fx avg `-0.001` n `6`; index avg `-0.003` n `26`; metal avg `-0.0021` n `20`; unknown avg `0.1802` n `1079`
- 1h: commodity avg `0.0094` n `13`; crypto_alt avg `0.1197` n `235`; crypto_major avg `0.0964` n `8`; equity avg `-0.0035` n `143`; fx avg `-0.022` n `6`; index avg `-0.006` n `26`; metal avg `0.0011` n `20`; unknown avg `0.1914` n `1049`
- 4h: commodity avg `-0.0417` n `13`; crypto_alt avg `0.6977` n `235`; crypto_major avg `0.2475` n `8`; equity avg `0.066` n `143`; fx avg `-0.0234` n `6`; index avg `-0.0013` n `26`; metal avg `0.0061` n `20`; unknown avg `0.399` n `1043`
- 24h: commodity avg `0.2101` n `13`; crypto_alt avg `1.9428` n `235`; crypto_major avg `0.9276` n `8`; equity avg `0.3039` n `143`; fx avg `-0.0473` n `6`; index avg `0.0192` n `26`; metal avg `0.0001` n `20`; unknown avg `0.3626` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
