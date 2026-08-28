# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T10:37:27.967188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.034` n `12`; crypto_alt avg `0.2751` n `231`; crypto_major avg `0.3183` n `8`; equity avg `0.0289` n `127`; fx avg `0.0317` n `6`; index avg `0.0021` n `26`; metal avg `0.0131` n `20`; unknown avg `0.0409` n `792`
- 1h: commodity avg `0.0218` n `12`; crypto_alt avg `0.1272` n `231`; crypto_major avg `0.0002` n `8`; equity avg `0.0452` n `127`; fx avg `0.0233` n `6`; index avg `0.0001` n `26`; metal avg `0.0486` n `20`; unknown avg `0.0485` n `792`
- 4h: commodity avg `0.0167` n `12`; crypto_alt avg `-0.4329` n `231`; crypto_major avg `-0.7951` n `8`; equity avg `-0.1457` n `127`; fx avg `0.0183` n `6`; index avg `0.0061` n `26`; metal avg `0.3385` n `20`; unknown avg `0.0223` n `792`
- 24h: commodity avg `0.1694` n `12`; crypto_alt avg `-0.1163` n `231`; crypto_major avg `0.0947` n `8`; equity avg `-0.9559` n `127`; fx avg `-0.0567` n `6`; index avg `-0.0094` n `26`; metal avg `0.7838` n `20`; unknown avg `0.3665` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
