# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T18:02:55.013698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `0.0893` n `230`; crypto_major avg `0.025` n `8`; equity avg `-0.0282` n `112`; fx avg `-0.0012` n `6`; index avg `0.0048` n `25`; metal avg `-0.0027` n `20`; unknown avg `0.0087` n `785`
- 1h: commodity avg `0.0093` n `12`; crypto_alt avg `0.0777` n `230`; crypto_major avg `-0.1032` n `8`; equity avg `0.0152` n `112`; fx avg `-0.0022` n `6`; index avg `0.0115` n `25`; metal avg `-0.0028` n `20`; unknown avg `-0.0043` n `785`
- 4h: commodity avg `-0.0356` n `12`; crypto_alt avg `0.7553` n `230`; crypto_major avg `0.1533` n `8`; equity avg `0.0738` n `112`; fx avg `0.0105` n `6`; index avg `0.022` n `25`; metal avg `0.0216` n `20`; unknown avg `-0.0086` n `785`
- 24h: commodity avg `0.0467` n `12`; crypto_alt avg `1.3151` n `230`; crypto_major avg `0.0986` n `8`; equity avg `0.246` n `112`; fx avg `0.0067` n `6`; index avg `0.0379` n `25`; metal avg `0.0623` n `20`; unknown avg `0.4424` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
