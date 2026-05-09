# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T01:52:22.336474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `0.1027` n `228`; crypto_major avg `0.1652` n `8`; equity avg `0.0256` n `65`; fx avg `0.0` n `5`; index avg `0.0279` n `23`; metal avg `0.0326` n `18`; unknown avg `0.6141` n `375`
- 1h: commodity avg `0.0019` n `12`; crypto_alt avg `0.6411` n `228`; crypto_major avg `0.6976` n `8`; equity avg `0.0696` n `65`; fx avg `0.0151` n `5`; index avg `0.127` n `23`; metal avg `0.1345` n `18`; unknown avg `0.4149` n `375`
- 4h: commodity avg `-0.1592` n `12`; crypto_alt avg `1.2831` n `228`; crypto_major avg `0.8486` n `8`; equity avg `0.1989` n `65`; fx avg `0.0047` n `5`; index avg `0.1022` n `23`; metal avg `-0.0477` n `18`; unknown avg `-0.0584` n `375`
- 24h: commodity avg `-0.4665` n `12`; crypto_alt avg `5.0103` n `228`; crypto_major avg `2.7984` n `8`; equity avg `3.6725` n `65`; fx avg `0.1171` n `5`; index avg `1.2796` n `23`; metal avg `0.1689` n `18`; unknown avg `1.3021` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
