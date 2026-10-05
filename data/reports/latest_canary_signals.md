# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T23:22:34.507513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `13`; crypto_alt avg `-0.1237` n `235`; crypto_major avg `-0.1147` n `8`; equity avg `0.0306` n `144`; fx avg `-0.0` n `6`; index avg `0.0123` n `26`; metal avg `0.0052` n `20`; unknown avg `0.1097` n `1079`
- 1h: commodity avg `-0.0147` n `13`; crypto_alt avg `-0.3301` n `235`; crypto_major avg `-0.2989` n `8`; equity avg `0.0255` n `144`; fx avg `-0.0167` n `6`; index avg `0.0094` n `26`; metal avg `-0.0388` n `20`; unknown avg `-0.0711` n `1077`
- 4h: commodity avg `0.0311` n `13`; crypto_alt avg `0.6053` n `235`; crypto_major avg `0.5655` n `8`; equity avg `0.2199` n `144`; fx avg `0.0093` n `6`; index avg `0.013` n `26`; metal avg `-0.0394` n `20`; unknown avg `-0.1897` n `979`
- 24h: commodity avg `-0.2187` n `13`; crypto_alt avg `0.2931` n `235`; crypto_major avg `-0.0304` n `8`; equity avg `0.2486` n `144`; fx avg `-0.0651` n `6`; index avg `0.1286` n `26`; metal avg `0.0935` n `20`; unknown avg `630.2859` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1966`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
