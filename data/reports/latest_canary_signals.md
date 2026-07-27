# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T08:22:29.001284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0658` n `12`; crypto_alt avg `-0.0688` n `230`; crypto_major avg `-0.0071` n `8`; equity avg `-0.0213` n `100`; fx avg `0.0144` n `6`; index avg `0.0006` n `25`; metal avg `-0.0046` n `20`; unknown avg `0.0359` n `775`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `-0.3397` n `230`; crypto_major avg `-0.224` n `8`; equity avg `-0.0903` n `100`; fx avg `0.0155` n `6`; index avg `-0.0196` n `25`; metal avg `-0.1289` n `20`; unknown avg `-0.0655` n `775`
- 4h: commodity avg `-0.3431` n `12`; crypto_alt avg `-0.3786` n `230`; crypto_major avg `-0.1724` n `8`; equity avg `0.4731` n `100`; fx avg `0.0127` n `6`; index avg `0.0748` n `25`; metal avg `0.1375` n `20`; unknown avg `-0.0242` n `759`
- 24h: commodity avg `-0.8036` n `12`; crypto_alt avg `0.535` n `230`; crypto_major avg `1.3441` n `8`; equity avg `1.3577` n `100`; fx avg `0.13` n `6`; index avg `0.1641` n `25`; metal avg `0.4123` n `20`; unknown avg `-0.0608` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
