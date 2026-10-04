# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T15:22:26.804992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `13`; crypto_alt avg `-0.0368` n `235`; crypto_major avg `0.0791` n `8`; equity avg `0.0002` n `144`; fx avg `0.002` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0005` n `20`; unknown avg `-0.0169` n `1078`
- 1h: commodity avg `-0.0154` n `13`; crypto_alt avg `0.1843` n `235`; crypto_major avg `0.3078` n `8`; equity avg `0.0259` n `144`; fx avg `0.0035` n `6`; index avg `-0.0107` n `26`; metal avg `0.0055` n `20`; unknown avg `0.5625` n `1076`
- 4h: commodity avg `-0.0463` n `13`; crypto_alt avg `0.1503` n `235`; crypto_major avg `0.1261` n `8`; equity avg `0.0408` n `144`; fx avg `0.0053` n `6`; index avg `-0.0203` n `26`; metal avg `0.0032` n `20`; unknown avg `0.0014` n `1070`
- 24h: commodity avg `-0.0192` n `13`; crypto_alt avg `1.3152` n `235`; crypto_major avg `1.0288` n `8`; equity avg `0.2848` n `144`; fx avg `0.0146` n `6`; index avg `0.0111` n `26`; metal avg `0.0135` n `20`; unknown avg `0.069` n `1019`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2046`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
