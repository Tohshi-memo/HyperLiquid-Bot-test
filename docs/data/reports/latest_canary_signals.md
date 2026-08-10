# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T02:52:24.501597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `0.2466` n `230`; crypto_major avg `0.2514` n `8`; equity avg `0.137` n `112`; fx avg `0.0067` n `6`; index avg `0.0427` n `25`; metal avg `-0.0372` n `20`; unknown avg `-0.1294` n `785`
- 1h: commodity avg `-0.0095` n `12`; crypto_alt avg `-0.2485` n `230`; crypto_major avg `-0.2093` n `8`; equity avg `-0.1281` n `112`; fx avg `-0.005` n `6`; index avg `-0.0173` n `25`; metal avg `0.0186` n `20`; unknown avg `0.0261` n `785`
- 4h: commodity avg `0.0283` n `12`; crypto_alt avg `-0.1271` n `230`; crypto_major avg `0.0186` n `8`; equity avg `-0.1934` n `112`; fx avg `0.1167` n `6`; index avg `0.0521` n `25`; metal avg `-0.1169` n `20`; unknown avg `-0.0946` n `785`
- 24h: commodity avg `0.4128` n `12`; crypto_alt avg `0.8949` n `230`; crypto_major avg `0.2181` n `8`; equity avg `-0.1934` n `112`; fx avg `0.1147` n `6`; index avg `0.0353` n `25`; metal avg `-0.1917` n `20`; unknown avg `-0.2927` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
