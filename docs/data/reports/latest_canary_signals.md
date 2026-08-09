# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T21:45:03.187642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.0062` n `230`; crypto_major avg `0.0135` n `8`; equity avg `-0.0008` n `112`; fx avg `0.0043` n `6`; index avg `0.0045` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.0175` n `785`
- 1h: commodity avg `0.0843` n `12`; crypto_alt avg `0.0359` n `230`; crypto_major avg `0.1004` n `8`; equity avg `0.0052` n `112`; fx avg `-0.0068` n `6`; index avg `0.0009` n `25`; metal avg `-0.0746` n `20`; unknown avg `-0.041` n `785`
- 4h: commodity avg `0.2402` n `12`; crypto_alt avg `0.249` n `230`; crypto_major avg `0.0603` n `8`; equity avg `0.0828` n `112`; fx avg `-0.0018` n `6`; index avg `0.0123` n `25`; metal avg `-0.047` n `20`; unknown avg `-0.4147` n `785`
- 24h: commodity avg `0.2423` n `12`; crypto_alt avg `1.405` n `230`; crypto_major avg `0.2271` n `8`; equity avg `0.2206` n `112`; fx avg `0.0031` n `6`; index avg `0.0357` n `25`; metal avg `0.0226` n `20`; unknown avg `-0.2731` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
