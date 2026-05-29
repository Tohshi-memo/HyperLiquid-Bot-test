# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T20:37:19.127935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `0.1318` n `228`; crypto_major avg `0.0232` n `8`; equity avg `0.0461` n `69`; fx avg `-0.0304` n `6`; index avg `-0.0108` n `23`; metal avg `-0.0367` n `18`; unknown avg `-0.0146` n `419`
- 1h: commodity avg `0.0485` n `12`; crypto_alt avg `0.3288` n `228`; crypto_major avg `0.0318` n `8`; equity avg `0.26` n `69`; fx avg `-0.0107` n `6`; index avg `0.0054` n `23`; metal avg `-0.1459` n `18`; unknown avg `-0.3903` n `419`
- 4h: commodity avg `0.2454` n `12`; crypto_alt avg `-0.4995` n `228`; crypto_major avg `-0.462` n `8`; equity avg `0.0324` n `69`; fx avg `0.0088` n `6`; index avg `0.086` n `23`; metal avg `-0.29` n `18`; unknown avg `-0.3168` n `419`
- 24h: commodity avg `-0.6902` n `12`; crypto_alt avg `0.6994` n `228`; crypto_major avg `1.0537` n `8`; equity avg `1.3641` n `69`; fx avg `0.2015` n `6`; index avg `0.1703` n `23`; metal avg `0.1142` n `18`; unknown avg `0.6202` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
