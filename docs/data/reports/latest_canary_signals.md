# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T13:52:37.762902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1` n `12`; crypto_alt avg `0.0013` n `234`; crypto_major avg `0.0051` n `8`; equity avg `-0.1176` n `140`; fx avg `0.0107` n `6`; index avg `-0.0675` n `26`; metal avg `-0.1464` n `20`; unknown avg `1.7901` n `918`
- 1h: commodity avg `-0.0239` n `12`; crypto_alt avg `-0.1122` n `234`; crypto_major avg `0.3123` n `8`; equity avg `-0.3272` n `140`; fx avg `-0.0059` n `6`; index avg `-0.0894` n `26`; metal avg `-0.1814` n `20`; unknown avg `14.8112` n `916`
- 4h: commodity avg `0.1429` n `12`; crypto_alt avg `-0.9767` n `234`; crypto_major avg `-0.3683` n `8`; equity avg `-0.7266` n `140`; fx avg `0.0146` n `6`; index avg `-0.1478` n `26`; metal avg `-0.3467` n `20`; unknown avg `9.4032` n `909`
- 24h: commodity avg `0.569` n `12`; crypto_alt avg `1.807` n `234`; crypto_major avg `-0.5481` n `8`; equity avg `-0.731` n `140`; fx avg `0.0197` n `6`; index avg `-0.2042` n `26`; metal avg `-0.6685` n `20`; unknown avg `3.9028` n `824`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
