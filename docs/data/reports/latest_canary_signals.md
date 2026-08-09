# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T21:37:26.403148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `0.0519` n `230`; crypto_major avg `0.1397` n `8`; equity avg `0.0324` n `112`; fx avg `0.0018` n `6`; index avg `0.0003` n `25`; metal avg `-0.0379` n `20`; unknown avg `-0.0206` n `785`
- 1h: commodity avg `0.1293` n `12`; crypto_alt avg `0.0431` n `230`; crypto_major avg `0.0993` n `8`; equity avg `0.0372` n `112`; fx avg `-0.013` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0821` n `20`; unknown avg `-0.1397` n `785`
- 4h: commodity avg `0.2299` n `12`; crypto_alt avg `0.2206` n `230`; crypto_major avg `-0.0385` n `8`; equity avg `0.1039` n `112`; fx avg `0.0004` n `6`; index avg `0.0138` n `25`; metal avg `-0.0451` n `20`; unknown avg `-0.3702` n `785`
- 24h: commodity avg `0.2607` n `12`; crypto_alt avg `1.4515` n `230`; crypto_major avg `0.1776` n `8`; equity avg `0.2196` n `112`; fx avg `-0.0013` n `6`; index avg `0.0332` n `25`; metal avg `0.0281` n `20`; unknown avg `-0.274` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
