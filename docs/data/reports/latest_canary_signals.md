# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T23:22:39.183790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `13`; crypto_alt avg `0.2028` n `239`; crypto_major avg `0.1477` n `8`; equity avg `0.1048` n `158`; fx avg `0.0131` n `6`; index avg `0.0099` n `27`; metal avg `-0.0078` n `20`; unknown avg `0.1865` n `1262`
- 1h: commodity avg `-0.0264` n `13`; crypto_alt avg `0.2696` n `239`; crypto_major avg `0.0976` n `8`; equity avg `0.234` n `158`; fx avg `0.0002` n `6`; index avg `0.0291` n `27`; metal avg `0.0108` n `20`; unknown avg `143.9298` n `1202`
- 4h: commodity avg `0.168` n `13`; crypto_alt avg `0.4553` n `239`; crypto_major avg `0.2369` n `8`; equity avg `1.3071` n `158`; fx avg `-0.0229` n `6`; index avg `0.1174` n `27`; metal avg `0.0484` n `20`; unknown avg `20.5816` n `1157`
- 24h: commodity avg `0.395` n `13`; crypto_alt avg `1.4587` n `239`; crypto_major avg `1.4733` n `8`; equity avg `2.3457` n `158`; fx avg `0.0827` n `6`; index avg `0.2169` n `27`; metal avg `-0.4726` n `20`; unknown avg `0.0352` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
