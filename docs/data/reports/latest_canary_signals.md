# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T07:37:28.978790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.0723` n `231`; crypto_major avg `-0.0957` n `8`; equity avg `-0.0155` n `128`; fx avg `-0.0017` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0029` n `20`; unknown avg `-0.0293` n `793`
- 1h: commodity avg `-0.0403` n `12`; crypto_alt avg `-0.1954` n `231`; crypto_major avg `-0.1524` n `8`; equity avg `-0.0236` n `128`; fx avg `-0.0041` n `6`; index avg `0.0038` n `26`; metal avg `-0.0027` n `20`; unknown avg `-0.0067` n `791`
- 4h: commodity avg `-0.0044` n `12`; crypto_alt avg `-0.057` n `231`; crypto_major avg `-0.0807` n `8`; equity avg `0.0239` n `128`; fx avg `0.0062` n `6`; index avg `0.012` n `26`; metal avg `0.0085` n `20`; unknown avg `-0.0034` n `759`
- 24h: commodity avg `-0.0262` n `12`; crypto_alt avg `0.646` n `231`; crypto_major avg `0.8674` n `8`; equity avg `0.2509` n `128`; fx avg `0.0027` n `6`; index avg `0.0647` n `26`; metal avg `0.1063` n `20`; unknown avg `0.7592` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1699`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
