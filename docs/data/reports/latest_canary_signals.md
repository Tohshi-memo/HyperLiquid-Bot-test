# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T09:07:28.558443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `0.0201` n `230`; crypto_major avg `0.0463` n `8`; equity avg `-0.0198` n `113`; fx avg `0.0004` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0499` n `20`; unknown avg `-0.0217` n `785`
- 1h: commodity avg `0.045` n `12`; crypto_alt avg `0.0925` n `230`; crypto_major avg `0.1379` n `8`; equity avg `-0.2515` n `113`; fx avg `0.009` n `6`; index avg `-0.0162` n `25`; metal avg `0.0468` n `20`; unknown avg `0.0107` n `785`
- 4h: commodity avg `0.36` n `12`; crypto_alt avg `-0.3716` n `230`; crypto_major avg `0.0029` n `8`; equity avg `-0.5503` n `113`; fx avg `0.0333` n `6`; index avg `-0.0826` n `25`; metal avg `-0.1363` n `20`; unknown avg `-0.0108` n `753`
- 24h: commodity avg `1.0844` n `12`; crypto_alt avg `-1.2397` n `230`; crypto_major avg `-0.8616` n `8`; equity avg `-1.611` n `113`; fx avg `0.0107` n `6`; index avg `-0.0657` n `25`; metal avg `0.2303` n `20`; unknown avg `0.1338` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1705`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
