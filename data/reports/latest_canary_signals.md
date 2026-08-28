# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T11:17:50.199477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0445` n `12`; crypto_alt avg `0.0025` n `231`; crypto_major avg `0.0339` n `8`; equity avg `-0.0105` n `127`; fx avg `0.0003` n `6`; index avg `0.0046` n `26`; metal avg `0.0244` n `20`; unknown avg `-0.0077` n `792`
- 1h: commodity avg `-0.0707` n `12`; crypto_alt avg `0.811` n `231`; crypto_major avg `0.8363` n `8`; equity avg `0.0867` n `127`; fx avg `0.0601` n `6`; index avg `0.0045` n `26`; metal avg `0.0121` n `20`; unknown avg `0.139` n `792`
- 4h: commodity avg `-0.0409` n `12`; crypto_alt avg `0.3645` n `231`; crypto_major avg `0.0008` n `8`; equity avg `-0.075` n `127`; fx avg `0.069` n `6`; index avg `-0.0163` n `26`; metal avg `0.1716` n `20`; unknown avg `0.0018` n `792`
- 24h: commodity avg `0.0712` n `12`; crypto_alt avg `-0.1437` n `231`; crypto_major avg `0.1459` n `8`; equity avg `-0.9493` n `127`; fx avg `-0.0171` n `6`; index avg `-0.033` n `26`; metal avg `0.6898` n `20`; unknown avg `0.3826` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
