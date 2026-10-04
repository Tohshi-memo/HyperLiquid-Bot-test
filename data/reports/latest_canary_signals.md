# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T13:52:26.969168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `13`; crypto_alt avg `0.009` n `235`; crypto_major avg `-0.0403` n `8`; equity avg `0.0082` n `144`; fx avg `0.0018` n `6`; index avg `0.0001` n `26`; metal avg `-0.0051` n `20`; unknown avg `1.0538` n `1078`
- 1h: commodity avg `-0.0089` n `13`; crypto_alt avg `-0.0262` n `235`; crypto_major avg `0.1225` n `8`; equity avg `0.0287` n `144`; fx avg `-0.0022` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0042` n `20`; unknown avg `0.4931` n `1076`
- 4h: commodity avg `0.0367` n `13`; crypto_alt avg `-0.1347` n `235`; crypto_major avg `0.0069` n `8`; equity avg `0.0547` n `144`; fx avg `0.0256` n `6`; index avg `0.0` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.0986` n `1070`
- 24h: commodity avg `0.1038` n `13`; crypto_alt avg `1.4386` n `235`; crypto_major avg `1.182` n `8`; equity avg `0.2891` n `144`; fx avg `0.0096` n `6`; index avg `0.0259` n `26`; metal avg `-0.0002` n `20`; unknown avg `-0.0663` n `915`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2059`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1784`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
