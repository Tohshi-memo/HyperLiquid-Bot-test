# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T15:52:29.240973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3717` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7203` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1203` n `12`; crypto_alt avg `-0.3374` n `228`; crypto_major avg `-0.3272` n `8`; equity avg `-0.1116` n `86`; fx avg `0.0223` n `6`; index avg `-0.0256` n `23`; metal avg `-0.0819` n `20`; unknown avg `0.0586` n `765`
- 1h: commodity avg `0.0717` n `12`; crypto_alt avg `0.5935` n `228`; crypto_major avg `0.6433` n `8`; equity avg `0.4289` n `86`; fx avg `-0.0174` n `6`; index avg `0.0577` n `23`; metal avg `-0.0385` n `20`; unknown avg `-0.0763` n `765`
- 4h: commodity avg `-0.2186` n `12`; crypto_alt avg `1.7615` n `228`; crypto_major avg `2.1531` n `8`; equity avg `1.5531` n `86`; fx avg `-0.0185` n `6`; index avg `0.1838` n `23`; metal avg `0.4328` n `20`; unknown avg `0.3062` n `765`
- 24h: commodity avg `-0.359` n `12`; crypto_alt avg `1.626` n `228`; crypto_major avg `2.3577` n `8`; equity avg `-0.3229` n `86`; fx avg `-0.0319` n `6`; index avg `-0.2044` n `23`; metal avg `0.4083` n `20`; unknown avg `0.2429` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
