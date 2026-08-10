# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T20:52:33.330317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.0508` n `230`; crypto_major avg `-0.0229` n `8`; equity avg `0.0287` n `113`; fx avg `-0.0056` n `6`; index avg `0.0086` n `25`; metal avg `-0.0094` n `20`; unknown avg `0.0442` n `785`
- 1h: commodity avg `0.0375` n `12`; crypto_alt avg `-0.0434` n `230`; crypto_major avg `0.0377` n `8`; equity avg `-0.1571` n `113`; fx avg `-0.0044` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0303` n `20`; unknown avg `1.0636` n `785`
- 4h: commodity avg `0.1535` n `12`; crypto_alt avg `0.0793` n `230`; crypto_major avg `0.6391` n `8`; equity avg `-0.2804` n `113`; fx avg `0.0258` n `6`; index avg `-0.0103` n `25`; metal avg `0.2393` n `20`; unknown avg `0.3891` n `785`
- 24h: commodity avg `1.1627` n `12`; crypto_alt avg `-1.027` n `230`; crypto_major avg `-0.9294` n `8`; equity avg `-1.7283` n `113`; fx avg `0.2545` n `6`; index avg `-0.094` n `25`; metal avg `0.1667` n `20`; unknown avg `103.7528` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
