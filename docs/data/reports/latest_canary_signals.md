# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T18:07:28.299239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `0.1078` n `230`; crypto_major avg `0.0273` n `8`; equity avg `0.0093` n `112`; fx avg `-0.0019` n `6`; index avg `0.0056` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.0042` n `785`
- 1h: commodity avg `0.0128` n `12`; crypto_alt avg `0.0958` n `230`; crypto_major avg `-0.1009` n `8`; equity avg `0.0528` n `112`; fx avg `-0.0028` n `6`; index avg `0.0123` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.0086` n `785`
- 4h: commodity avg `-0.032` n `12`; crypto_alt avg `0.773` n `230`; crypto_major avg `0.1556` n `8`; equity avg `0.1113` n `112`; fx avg `0.0098` n `6`; index avg `0.0229` n `25`; metal avg `0.0217` n `20`; unknown avg `-0.0095` n `785`
- 24h: commodity avg `0.0503` n `12`; crypto_alt avg `1.3345` n `230`; crypto_major avg `0.1009` n `8`; equity avg `0.2839` n `112`; fx avg `0.0061` n `6`; index avg `0.0387` n `25`; metal avg `0.0624` n `20`; unknown avg `0.4435` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
