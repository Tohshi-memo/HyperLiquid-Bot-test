# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T17:07:26.813034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.1508` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5662` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0702` n `12`; crypto_alt avg `0.1564` n `228`; crypto_major avg `0.1236` n `8`; equity avg `0.1233` n `86`; fx avg `0.0001` n `6`; index avg `0.0165` n `23`; metal avg `0.047` n `20`; unknown avg `-0.0954` n `765`
- 1h: commodity avg `-0.0179` n `12`; crypto_alt avg `0.1823` n `228`; crypto_major avg `0.0466` n `8`; equity avg `0.1723` n `86`; fx avg `-0.0069` n `6`; index avg `0.0427` n `23`; metal avg `0.0024` n `20`; unknown avg `-0.1177` n `765`
- 4h: commodity avg `-0.1466` n `12`; crypto_alt avg `2.8277` n `228`; crypto_major avg `3.0042` n `8`; equity avg `2.1885` n `86`; fx avg `-0.0711` n `6`; index avg `0.3118` n `23`; metal avg `0.438` n `20`; unknown avg `0.6718` n `765`
- 24h: commodity avg `-0.3978` n `12`; crypto_alt avg `2.9055` n `228`; crypto_major avg `3.1981` n `8`; equity avg `-0.0123` n `86`; fx avg `-0.0576` n `6`; index avg `-0.1498` n `23`; metal avg `0.6132` n `20`; unknown avg `0.2104` n `701`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.209`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
