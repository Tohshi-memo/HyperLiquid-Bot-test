# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T00:52:17.675064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1213` n `12`; crypto_alt avg `-0.6916` n `228`; crypto_major avg `-0.606` n `8`; equity avg `-0.2019` n `67`; fx avg `0.0528` n `6`; index avg `-0.0449` n `23`; metal avg `-0.1565` n `18`; unknown avg `2.2911` n `407`
- 1h: commodity avg `0.3327` n `12`; crypto_alt avg `-1.2483` n `228`; crypto_major avg `-1.1101` n `8`; equity avg `-0.5647` n `67`; fx avg `-0.0094` n `6`; index avg `-0.184` n `23`; metal avg `-0.2723` n `18`; unknown avg `2.7239` n `405`
- 4h: commodity avg `0.3862` n `12`; crypto_alt avg `-1.6863` n `228`; crypto_major avg `-1.1818` n `8`; equity avg `-0.7934` n `67`; fx avg `0.0163` n `6`; index avg `-0.3732` n `23`; metal avg `-0.5597` n `18`; unknown avg `1.104` n `405`
- 24h: commodity avg `0.1421` n `12`; crypto_alt avg `-0.0694` n `228`; crypto_major avg `-1.257` n `8`; equity avg `-0.0461` n `67`; fx avg `0.0429` n `6`; index avg `0.1232` n `23`; metal avg `-0.1948` n `18`; unknown avg `0.6142` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
