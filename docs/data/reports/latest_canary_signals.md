# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T07:07:23.947108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0926` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7138` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0519` n `13`; crypto_alt avg `0.1451` n `239`; crypto_major avg `0.1616` n `8`; equity avg `0.3424` n `164`; fx avg `0.0181` n `6`; index avg `0.0332` n `27`; metal avg `0.104` n `20`; unknown avg `-0.0504` n `1260`
- 1h: commodity avg `-0.028` n `13`; crypto_alt avg `0.4974` n `239`; crypto_major avg `0.5227` n `8`; equity avg `0.7788` n `164`; fx avg `0.006` n `6`; index avg `0.0949` n `27`; metal avg `0.0453` n `20`; unknown avg `12.8306` n `1250`
- 4h: commodity avg `0.0468` n `13`; crypto_alt avg `1.3383` n `239`; crypto_major avg `2.1394` n `8`; equity avg `1.6817` n `164`; fx avg `0.0286` n `6`; index avg `0.2679` n `27`; metal avg `0.4256` n `20`; unknown avg `19.3025` n `1211`
- 24h: commodity avg `0.3792` n `13`; crypto_alt avg `0.056` n `239`; crypto_major avg `-0.421` n `8`; equity avg `0.3783` n `164`; fx avg `-0.071` n `6`; index avg `0.1842` n `27`; metal avg `-0.2792` n `20`; unknown avg `91.2094` n `1105`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
