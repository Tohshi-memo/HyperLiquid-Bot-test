# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T23:52:27.616691+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.044` n `231`; crypto_major avg `-0.033` n `8`; equity avg `-0.0386` n `127`; fx avg `-0.0053` n `6`; index avg `-0.0208` n `26`; metal avg `-0.0293` n `20`; unknown avg `0.0164` n `792`
- 1h: commodity avg `-0.0144` n `12`; crypto_alt avg `-0.0442` n `231`; crypto_major avg `0.0994` n `8`; equity avg `-0.1419` n `127`; fx avg `-0.002` n `6`; index avg `-0.0297` n `26`; metal avg `-0.0676` n `20`; unknown avg `-0.0965` n `792`
- 4h: commodity avg `-0.0203` n `12`; crypto_alt avg `0.1335` n `231`; crypto_major avg `0.211` n `8`; equity avg `-0.4699` n `127`; fx avg `0.0023` n `6`; index avg `-0.0347` n `26`; metal avg `-0.0607` n `20`; unknown avg `-0.1213` n `792`
- 24h: commodity avg `0.3385` n `12`; crypto_alt avg `0.711` n `231`; crypto_major avg `2.0168` n `8`; equity avg `-0.5571` n `127`; fx avg `-0.0203` n `6`; index avg `-0.173` n `26`; metal avg `-0.0029` n `20`; unknown avg `0.8287` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
