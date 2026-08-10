# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T22:22:36.199807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `0.1893` n `230`; crypto_major avg `0.0779` n `8`; equity avg `-0.054` n `113`; fx avg `-0.0042` n `6`; index avg `-0.021` n `25`; metal avg `0.0064` n `20`; unknown avg `0.0306` n `785`
- 1h: commodity avg `-0.0458` n `12`; crypto_alt avg `0.0843` n `230`; crypto_major avg `-0.1476` n `8`; equity avg `0.0033` n `113`; fx avg `0.0001` n `6`; index avg `-0.0117` n `25`; metal avg `-0.0139` n `20`; unknown avg `-0.113` n `785`
- 4h: commodity avg `-0.1262` n `12`; crypto_alt avg `-0.423` n `230`; crypto_major avg `0.0006` n `8`; equity avg `-0.3522` n `113`; fx avg `0.0116` n `6`; index avg `-0.0172` n `25`; metal avg `0.222` n `20`; unknown avg `2.9511` n `785`
- 24h: commodity avg `0.7911` n `12`; crypto_alt avg `-1.6016` n `230`; crypto_major avg `-1.4398` n `8`; equity avg `-1.7186` n `113`; fx avg `0.2625` n `6`; index avg `-0.0651` n `25`; metal avg `0.366` n `20`; unknown avg `103.6247` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
