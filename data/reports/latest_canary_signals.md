# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T01:07:19.161120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1235` n `12`; crypto_alt avg `0.102` n `228`; crypto_major avg `0.2809` n `8`; equity avg `-0.0719` n `67`; fx avg `-0.0558` n `6`; index avg `0.0155` n `23`; metal avg `-0.0807` n `18`; unknown avg `0.2311` n `407`
- 1h: commodity avg `0.2873` n `12`; crypto_alt avg `-1.01` n `228`; crypto_major avg `-0.7776` n `8`; equity avg `-0.1937` n `67`; fx avg `-0.0327` n `6`; index avg `-0.2077` n `23`; metal avg `-0.2093` n `18`; unknown avg `4.5624` n `407`
- 4h: commodity avg `0.5122` n `12`; crypto_alt avg `-1.613` n `228`; crypto_major avg `-1.0556` n `8`; equity avg `-0.8511` n `67`; fx avg `-0.1122` n `6`; index avg `-0.3937` n `23`; metal avg `-0.6591` n `18`; unknown avg `3.727` n `405`
- 24h: commodity avg `0.0923` n `12`; crypto_alt avg `0.0836` n `228`; crypto_major avg `-0.9083` n `8`; equity avg `-0.1425` n `67`; fx avg `-0.0163` n `6`; index avg `0.1334` n `23`; metal avg `-0.1882` n `18`; unknown avg `0.7873` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
