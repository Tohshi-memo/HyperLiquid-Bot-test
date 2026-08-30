# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T20:22:23.188781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0375` n `12`; crypto_alt avg `-0.0095` n `231`; crypto_major avg `-0.0438` n `8`; equity avg `-0.0064` n `128`; fx avg `0.0` n `6`; index avg `-0.0039` n `26`; metal avg `-0.0255` n `20`; unknown avg `0.0671` n `793`
- 1h: commodity avg `0.2442` n `12`; crypto_alt avg `-0.2872` n `231`; crypto_major avg `-0.3156` n `8`; equity avg `-0.0693` n `128`; fx avg `-0.0043` n `6`; index avg `0.0003` n `26`; metal avg `-0.0538` n `20`; unknown avg `0.2801` n `791`
- 4h: commodity avg `0.4181` n `12`; crypto_alt avg `0.0632` n `231`; crypto_major avg `-0.4002` n `8`; equity avg `-0.0608` n `128`; fx avg `-0.0017` n `6`; index avg `0.0018` n `26`; metal avg `-0.0534` n `20`; unknown avg `0.1044` n `791`
- 24h: commodity avg `0.4361` n `12`; crypto_alt avg `1.4045` n `231`; crypto_major avg `0.6644` n `8`; equity avg `0.1312` n `128`; fx avg `0.0274` n `6`; index avg `0.0473` n `26`; metal avg `0.0535` n `20`; unknown avg `0.1252` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
