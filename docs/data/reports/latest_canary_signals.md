# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T00:07:32.410720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.7002` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0035` n `13`; crypto_alt avg `0.1735` n `239`; crypto_major avg `0.1419` n `8`; equity avg `0.1573` n `165`; fx avg `0.0152` n `6`; index avg `0.0459` n `27`; metal avg `0.0818` n `20`; unknown avg `0.2006` n `1246`
- 1h: commodity avg `-0.0357` n `13`; crypto_alt avg `0.1454` n `239`; crypto_major avg `0.0504` n `8`; equity avg `-0.1562` n `165`; fx avg `0.0394` n `6`; index avg `0.0105` n `27`; metal avg `-0.1181` n `20`; unknown avg `23.6047` n `1250`
- 4h: commodity avg `0.0545` n `13`; crypto_alt avg `-0.1498` n `239`; crypto_major avg `-0.2924` n `8`; equity avg `-1.9926` n `165`; fx avg `0.012` n `6`; index avg `-0.0682` n `27`; metal avg `-0.4797` n `20`; unknown avg `10.4216` n `1228`
- 24h: commodity avg `0.0468` n `13`; crypto_alt avg `-0.8857` n `239`; crypto_major avg `-0.4533` n `8`; equity avg `-4.4242` n `165`; fx avg `0.034` n `6`; index avg `-0.2993` n `27`; metal avg `-1.095` n `20`; unknown avg `17.3137` n `1168`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
