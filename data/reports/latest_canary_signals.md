# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T18:52:27.958609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `-0.002` n `230`; crypto_major avg `-0.0057` n `8`; equity avg `0.0098` n `112`; fx avg `-0.0013` n `6`; index avg `0.0045` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.1442` n `785`
- 1h: commodity avg `0.0622` n `12`; crypto_alt avg `0.023` n `230`; crypto_major avg `-0.0613` n `8`; equity avg `0.0311` n `112`; fx avg `-0.0015` n `6`; index avg `0.0288` n `25`; metal avg `0.0026` n `20`; unknown avg `-0.162` n `785`
- 4h: commodity avg `0.0194` n `12`; crypto_alt avg `0.636` n `230`; crypto_major avg `0.0901` n `8`; equity avg `0.1159` n `112`; fx avg `0.0102` n `6`; index avg `0.0518` n `25`; metal avg `0.024` n `20`; unknown avg `-0.1632` n `785`
- 24h: commodity avg `0.0866` n `12`; crypto_alt avg `1.2619` n `230`; crypto_major avg `0.1745` n `8`; equity avg `0.3197` n `112`; fx avg `0.0002` n `6`; index avg `0.0645` n `25`; metal avg `0.0716` n `20`; unknown avg `0.2909` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
