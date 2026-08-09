# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T23:22:37.291848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `-0.3119` n `230`; crypto_major avg `-0.2759` n `8`; equity avg `-0.0481` n `112`; fx avg `-0.0133` n `6`; index avg `-0.0168` n `25`; metal avg `0.0019` n `20`; unknown avg `0.0432` n `785`
- 1h: commodity avg `-0.0499` n `12`; crypto_alt avg `-1.1191` n `230`; crypto_major avg `-0.9274` n `8`; equity avg `-0.0608` n `112`; fx avg `-0.0003` n `6`; index avg `-0.0016` n `25`; metal avg `0.0454` n `20`; unknown avg `1.4136` n `785`
- 4h: commodity avg `0.3012` n `12`; crypto_alt avg `-0.7098` n `230`; crypto_major avg `-0.7148` n `8`; equity avg `-0.141` n `112`; fx avg `-0.0025` n `6`; index avg `-0.0501` n `25`; metal avg `-0.117` n `20`; unknown avg `0.085` n `785`
- 24h: commodity avg `0.4086` n `12`; crypto_alt avg `0.6193` n `230`; crypto_major avg `-0.3101` n `8`; equity avg `0.0199` n `112`; fx avg `-0.003` n `6`; index avg `-0.0168` n `25`; metal avg `-0.051` n `20`; unknown avg `-0.3602` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
