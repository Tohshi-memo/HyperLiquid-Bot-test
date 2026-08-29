# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T15:22:27.964610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0227` n `12`; crypto_alt avg `-0.0992` n `231`; crypto_major avg `-0.0338` n `8`; equity avg `-0.0028` n `128`; fx avg `-0.003` n `6`; index avg `0.0029` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.0008` n `790`
- 1h: commodity avg `-0.0297` n `12`; crypto_alt avg `0.2366` n `231`; crypto_major avg `0.3937` n `8`; equity avg `0.0017` n `128`; fx avg `0.0058` n `6`; index avg `0.0134` n `26`; metal avg `0.025` n `20`; unknown avg `0.0629` n `782`
- 4h: commodity avg `-0.0184` n `12`; crypto_alt avg `0.8664` n `231`; crypto_major avg `0.7444` n `8`; equity avg `-0.0227` n `128`; fx avg `-0.0044` n `6`; index avg `0.0105` n `26`; metal avg `0.0475` n `20`; unknown avg `0.3989` n `764`
- 24h: commodity avg `0.0287` n `12`; crypto_alt avg `-1.5654` n `231`; crypto_major avg `-1.7045` n `8`; equity avg `-1.1263` n `128`; fx avg `-0.0579` n `6`; index avg `-0.2098` n `26`; metal avg `-0.6556` n `20`; unknown avg `-0.3296` n `732`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2104`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
