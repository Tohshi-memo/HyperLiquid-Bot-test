# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T20:26:45.697403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `0.0791` n `230`; crypto_major avg `-0.0714` n `8`; equity avg `0.0789` n `113`; fx avg `0.0014` n `6`; index avg `-0.0136` n `25`; metal avg `-0.001` n `20`; unknown avg `3.0674` n `785`
- 1h: commodity avg `0.0488` n `12`; crypto_alt avg `-0.0021` n `230`; crypto_major avg `0.1351` n `8`; equity avg `-0.3758` n `113`; fx avg `0.0141` n `6`; index avg `-0.0453` n `25`; metal avg `-0.0257` n `20`; unknown avg `2.7066` n `785`
- 4h: commodity avg `0.171` n `12`; crypto_alt avg `0.1154` n `230`; crypto_major avg `0.5206` n `8`; equity avg `-0.4735` n `113`; fx avg `0.0311` n `6`; index avg `-0.0634` n `25`; metal avg `0.1218` n `20`; unknown avg `0.9598` n `785`
- 24h: commodity avg `1.2002` n `12`; crypto_alt avg `-0.9663` n `230`; crypto_major avg `-0.8999` n `8`; equity avg `-1.6987` n `113`; fx avg `0.264` n `6`; index avg `-0.1037` n `25`; metal avg `0.1553` n `20`; unknown avg `103.5982` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
