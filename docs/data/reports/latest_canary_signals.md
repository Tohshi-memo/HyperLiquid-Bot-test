# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T22:37:29.944583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0621` n `12`; crypto_alt avg `-0.4645` n `230`; crypto_major avg `-0.5576` n `8`; equity avg `-0.1273` n `112`; fx avg `-0.0008` n `6`; index avg `-0.0159` n `25`; metal avg `0.0029` n `20`; unknown avg `0.5301` n `785`
- 1h: commodity avg `0.1785` n `12`; crypto_alt avg `-0.2313` n `230`; crypto_major avg `-0.4397` n `8`; equity avg `-0.2806` n `112`; fx avg `0.0029` n `6`; index avg `-0.0512` n `25`; metal avg `-0.1006` n `20`; unknown avg `0.5326` n `785`
- 4h: commodity avg `0.3577` n `12`; crypto_alt avg `-0.001` n `230`; crypto_major avg `-0.3376` n `8`; equity avg `-0.2192` n `112`; fx avg `-0.003` n `6`; index avg `-0.0676` n `25`; metal avg `-0.1515` n `20`; unknown avg `-0.2932` n `785`
- 24h: commodity avg `0.3846` n `12`; crypto_alt avg `1.2742` n `230`; crypto_major avg `-0.0643` n `8`; equity avg `-0.0671` n `112`; fx avg `-0.0019` n `6`; index avg `-0.02` n `25`; metal avg `-0.0722` n `20`; unknown avg `-0.3459` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
