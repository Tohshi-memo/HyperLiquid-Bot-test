# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T18:57:09.646121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0568` n `12`; crypto_alt avg `-0.0343` n `230`; crypto_major avg `-0.0077` n `8`; equity avg `-0.0177` n `112`; fx avg `0.0005` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.2216` n `785`
- 1h: commodity avg `0.1098` n `12`; crypto_alt avg `-0.0087` n `230`; crypto_major avg `-0.0634` n `8`; equity avg `0.0036` n `112`; fx avg `0.0003` n `6`; index avg `0.0207` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.2399` n `785`
- 4h: commodity avg `0.067` n `12`; crypto_alt avg `0.6027` n `230`; crypto_major avg `0.088` n `8`; equity avg `0.0883` n `112`; fx avg `0.012` n `6`; index avg `0.0437` n `25`; metal avg `0.0232` n `20`; unknown avg `-0.2368` n `785`
- 24h: commodity avg `0.1341` n `12`; crypto_alt avg `1.2278` n `230`; crypto_major avg `0.1724` n `8`; equity avg `0.2923` n `112`; fx avg `0.002` n `6`; index avg `0.0564` n `25`; metal avg `0.0707` n `20`; unknown avg `0.2151` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
