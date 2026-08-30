# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T18:52:27.961657+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `0.048` n `231`; crypto_major avg `-0.1538` n `8`; equity avg `-0.0066` n `128`; fx avg `0.0026` n `6`; index avg `0.0028` n `26`; metal avg `-0.0046` n `20`; unknown avg `-0.0041` n `793`
- 1h: commodity avg `0.0023` n `12`; crypto_alt avg `0.3584` n `231`; crypto_major avg `0.344` n `8`; equity avg `0.0117` n `128`; fx avg `0.0029` n `6`; index avg `-0.0169` n `26`; metal avg `-0.0095` n `20`; unknown avg `-0.0908` n `793`
- 4h: commodity avg `0.0634` n `12`; crypto_alt avg `0.6458` n `231`; crypto_major avg `0.5734` n `8`; equity avg `0.1209` n `128`; fx avg `0.0119` n `6`; index avg `0.0104` n `26`; metal avg `0.031` n `20`; unknown avg `0.6414` n `793`
- 24h: commodity avg `0.0472` n `12`; crypto_alt avg `1.8302` n `231`; crypto_major avg `1.1871` n `8`; equity avg `0.3658` n `128`; fx avg `0.0295` n `6`; index avg `0.091` n `26`; metal avg `0.1094` n `20`; unknown avg `0.1223` n `740`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
