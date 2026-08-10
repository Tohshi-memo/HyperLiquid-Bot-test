# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T03:37:25.628722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0324` n `12`; crypto_alt avg `0.027` n `230`; crypto_major avg `-0.0047` n `8`; equity avg `0.0435` n `112`; fx avg `-0.017` n `6`; index avg `0.002` n `25`; metal avg `0.0361` n `20`; unknown avg `-0.0094` n `785`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `0.2349` n `230`; crypto_major avg `0.1677` n `8`; equity avg `0.0884` n `112`; fx avg `-0.0221` n `6`; index avg `0.0366` n `25`; metal avg `0.0249` n `20`; unknown avg `-0.253` n `785`
- 4h: commodity avg `-0.0046` n `12`; crypto_alt avg `0.5357` n `230`; crypto_major avg `0.3639` n `8`; equity avg `-0.2332` n `112`; fx avg `0.0943` n `6`; index avg `0.0429` n `25`; metal avg `-0.0428` n `20`; unknown avg `-0.0434` n `785`
- 24h: commodity avg `0.4238` n `12`; crypto_alt avg `0.8208` n `230`; crypto_major avg `0.0861` n `8`; equity avg `-0.1775` n `112`; fx avg `0.0799` n `6`; index avg `0.0318` n `25`; metal avg `-0.1374` n `20`; unknown avg `-0.3038` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
