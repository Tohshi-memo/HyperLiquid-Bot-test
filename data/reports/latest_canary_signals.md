# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T18:07:30.320363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `13`; crypto_alt avg `0.053` n `235`; crypto_major avg `-0.0918` n `8`; equity avg `0.0257` n `144`; fx avg `-0.0` n `6`; index avg `0.008` n `26`; metal avg `0.006` n `20`; unknown avg `1.1213` n `1076`
- 1h: commodity avg `0.029` n `13`; crypto_alt avg `-0.0368` n `235`; crypto_major avg `0.0271` n `8`; equity avg `0.025` n `144`; fx avg `-0.0006` n `6`; index avg `0.0085` n `26`; metal avg `0.0072` n `20`; unknown avg `1.233` n `1076`
- 4h: commodity avg `0.118` n `13`; crypto_alt avg `0.1128` n `235`; crypto_major avg `0.327` n `8`; equity avg `0.035` n `144`; fx avg `0.0002` n `6`; index avg `-0.0125` n `26`; metal avg `0.0011` n `20`; unknown avg `1.0545` n `1070`
- 24h: commodity avg `0.0502` n `13`; crypto_alt avg `0.7724` n `235`; crypto_major avg `0.7611` n `8`; equity avg `0.2184` n `144`; fx avg `0.0219` n `6`; index avg `-0.0061` n `26`; metal avg `0.0042` n `20`; unknown avg `0.9688` n `1019`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.204`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
