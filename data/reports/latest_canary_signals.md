# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T07:32:22.173107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `-0.0795` n `231`; crypto_major avg `-0.0569` n `8`; equity avg `-0.0082` n `128`; fx avg `0.0` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0021` n `20`; unknown avg `-0.0265` n `793`
- 1h: commodity avg `-0.0345` n `12`; crypto_alt avg `-0.2026` n `231`; crypto_major avg `-0.1137` n `8`; equity avg `-0.0163` n `128`; fx avg `-0.0025` n `6`; index avg `0.0056` n `26`; metal avg `-0.0019` n `20`; unknown avg `-0.0028` n `791`
- 4h: commodity avg `0.0014` n `12`; crypto_alt avg `-0.064` n `231`; crypto_major avg `-0.0419` n `8`; equity avg `0.0312` n `128`; fx avg `0.0079` n `6`; index avg `0.0138` n `26`; metal avg `0.0093` n `20`; unknown avg `0.0001` n `759`
- 24h: commodity avg `-0.0204` n `12`; crypto_alt avg `0.6393` n `231`; crypto_major avg `0.9068` n `8`; equity avg `0.2582` n `128`; fx avg `0.0044` n `6`; index avg `0.0665` n `26`; metal avg `0.1071` n `20`; unknown avg `0.7618` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1699`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
