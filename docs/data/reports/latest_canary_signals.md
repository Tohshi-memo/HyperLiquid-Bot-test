# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T04:37:37.228302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.0746` n `230`; crypto_major avg `-0.0595` n `8`; equity avg `-0.0669` n `112`; fx avg `0.0056` n `6`; index avg `-0.021` n `25`; metal avg `-0.016` n `20`; unknown avg `1.1652` n `785`
- 1h: commodity avg `-0.0348` n `12`; crypto_alt avg `-0.0686` n `230`; crypto_major avg `-0.1576` n `8`; equity avg `-0.045` n `112`; fx avg `0.0182` n `6`; index avg `-0.0233` n `25`; metal avg `0.0366` n `20`; unknown avg `1.1377` n `785`
- 4h: commodity avg `-0.0199` n `12`; crypto_alt avg `0.177` n `230`; crypto_major avg `0.1377` n `8`; equity avg `-0.1773` n `112`; fx avg `0.0425` n `6`; index avg `0.0072` n `25`; metal avg `0.046` n `20`; unknown avg `0.5249` n `785`
- 24h: commodity avg `0.3268` n `12`; crypto_alt avg `0.4377` n `230`; crypto_major avg `-0.1147` n `8`; equity avg `-0.223` n `112`; fx avg `0.1026` n `6`; index avg `0.0046` n `25`; metal avg `-0.0929` n `20`; unknown avg `-0.3259` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
