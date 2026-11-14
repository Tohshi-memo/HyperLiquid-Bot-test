# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T13:22:27.806817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0083` n `13`; crypto_alt avg `0.0342` n `239`; crypto_major avg `-0.0635` n `8`; equity avg `0.0016` n `162`; fx avg `0.0044` n `6`; index avg `-0.0028` n `27`; metal avg `-0.0088` n `20`; unknown avg `0.1377` n `1260`
- 1h: commodity avg `-0.0119` n `13`; crypto_alt avg `-0.3654` n `239`; crypto_major avg `-0.4854` n `8`; equity avg `-0.119` n `162`; fx avg `-0.0018` n `6`; index avg `-0.0073` n `27`; metal avg `-0.019` n `20`; unknown avg `-0.3023` n `1260`
- 4h: commodity avg `-0.0492` n `13`; crypto_alt avg `-0.5391` n `239`; crypto_major avg `-0.3653` n `8`; equity avg `-0.0844` n `162`; fx avg `0.0152` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0108` n `20`; unknown avg `81.224` n `1228`
- 24h: commodity avg `-0.1595` n `13`; crypto_alt avg `-3.8502` n `239`; crypto_major avg `-4.2396` n `8`; equity avg `-2.9275` n `162`; fx avg `-0.1312` n `6`; index avg `-0.2442` n `27`; metal avg `-0.375` n `20`; unknown avg `0.5026` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
