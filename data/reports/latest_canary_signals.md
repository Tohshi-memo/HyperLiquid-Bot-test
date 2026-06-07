# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T14:22:21.689268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `71.18` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0777` n `12`; crypto_alt avg `0.56` n `228`; crypto_major avg `0.4648` n `8`; equity avg `0.2353` n `74`; fx avg `0.0023` n `6`; index avg `0.0733` n `23`; metal avg `0.0636` n `18`; unknown avg `0.1024` n `516`
- 1h: commodity avg `-0.0222` n `12`; crypto_alt avg `0.8939` n `228`; crypto_major avg `0.7775` n `8`; equity avg `0.6652` n `74`; fx avg `0.0003` n `6`; index avg `0.2568` n `23`; metal avg `0.1257` n `18`; unknown avg `0.1662` n `516`
- 4h: commodity avg `0.2168` n `12`; crypto_alt avg `-0.2401` n `228`; crypto_major avg `-0.3865` n `8`; equity avg `0.61` n `74`; fx avg `0.0155` n `6`; index avg `0.3995` n `23`; metal avg `-0.0705` n `18`; unknown avg `0.1109` n `516`
- 24h: commodity avg `0.1329` n `12`; crypto_alt avg `1.8388` n `228`; crypto_major avg `2.0646` n `8`; equity avg `1.7663` n `74`; fx avg `0.0269` n `6`; index avg `0.4282` n `23`; metal avg `0.6423` n `18`; unknown avg `-2.7508` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
