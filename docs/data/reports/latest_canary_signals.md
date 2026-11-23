# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T04:52:29.042548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0278` n `13`; crypto_alt avg `0.0267` n `239`; crypto_major avg `0.0085` n `8`; equity avg `0.0511` n `166`; fx avg `-0.0206` n `6`; index avg `0.0204` n `27`; metal avg `0.0214` n `20`; unknown avg `-0.3124` n `1266`
- 1h: commodity avg `0.0194` n `13`; crypto_alt avg `0.1561` n `239`; crypto_major avg `0.0051` n `8`; equity avg `0.1285` n `166`; fx avg `-0.0181` n `6`; index avg `-0.0017` n `27`; metal avg `0.0468` n `20`; unknown avg `10.4384` n `1254`
- 4h: commodity avg `0.063` n `13`; crypto_alt avg `0.468` n `239`; crypto_major avg `0.3155` n `8`; equity avg `0.1953` n `166`; fx avg `0.1252` n `6`; index avg `-0.0786` n `27`; metal avg `0.0546` n `20`; unknown avg `3.0568` n `1243`
- 24h: commodity avg `-0.3316` n `13`; crypto_alt avg `1.9066` n `239`; crypto_major avg `2.5559` n `8`; equity avg `2.0942` n `166`; fx avg `0.2202` n `6`; index avg `0.1811` n `27`; metal avg `0.4164` n `20`; unknown avg `293.492` n `1025`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
