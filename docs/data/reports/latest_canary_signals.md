# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T21:37:25.361137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.034` n `12`; crypto_alt avg `0.302` n `231`; crypto_major avg `0.199` n `8`; equity avg `0.0091` n `128`; fx avg `0.0036` n `6`; index avg `0.0094` n `26`; metal avg `-0.019` n `20`; unknown avg `-0.025` n `793`
- 1h: commodity avg `0.0478` n `12`; crypto_alt avg `-0.3616` n `231`; crypto_major avg `-0.5896` n `8`; equity avg `-0.0751` n `128`; fx avg `0.0042` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0488` n `20`; unknown avg `0.346` n `789`
- 4h: commodity avg `0.4898` n `12`; crypto_alt avg `-0.6386` n `231`; crypto_major avg `-0.9789` n `8`; equity avg `-0.1987` n `128`; fx avg `-0.0057` n `6`; index avg `-0.0414` n `26`; metal avg `-0.1147` n `20`; unknown avg `0.0073` n `791`
- 24h: commodity avg `0.5282` n `12`; crypto_alt avg `1.0597` n `231`; crypto_major avg `0.0101` n `8`; equity avg `-0.0087` n `128`; fx avg `0.0351` n `6`; index avg `0.0205` n `26`; metal avg `0.0004` n `20`; unknown avg `0.0511` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
