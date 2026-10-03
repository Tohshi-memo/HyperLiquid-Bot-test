# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T10:07:28.813248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `0.1532` n `235`; crypto_major avg `-0.0256` n `8`; equity avg `0.0078` n `143`; fx avg `0.0001` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0052` n `20`; unknown avg `0.044` n `982`
- 1h: commodity avg `0.0326` n `13`; crypto_alt avg `0.5051` n `235`; crypto_major avg `0.0733` n `8`; equity avg `0.0074` n `143`; fx avg `-0.0134` n `6`; index avg `-0.0016` n `26`; metal avg `-0.007` n `20`; unknown avg `1.0393` n `982`
- 4h: commodity avg `0.0863` n `13`; crypto_alt avg `-0.0674` n `235`; crypto_major avg `-0.1023` n `8`; equity avg `0.0266` n `143`; fx avg `-0.0095` n `6`; index avg `-0.008` n `26`; metal avg `-0.0079` n `20`; unknown avg `2.0997` n `966`
- 24h: commodity avg `0.7548` n `13`; crypto_alt avg `-2.0645` n `235`; crypto_major avg `-2.3347` n `8`; equity avg `0.0759` n `142`; fx avg `0.0023` n `6`; index avg `0.1381` n `26`; metal avg `-0.2561` n `20`; unknown avg `-0.3956` n `872`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
