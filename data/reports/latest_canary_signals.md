# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T09:52:21.263053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.0973` n `228`; crypto_major avg `-0.0763` n `8`; equity avg `-0.0309` n `69`; fx avg `0.0087` n `6`; index avg `-0.0107` n `23`; metal avg `0.1213` n `18`; unknown avg `-0.327` n `417`
- 1h: commodity avg `-0.6367` n `12`; crypto_alt avg `0.3895` n `228`; crypto_major avg `0.1798` n `8`; equity avg `0.1399` n `69`; fx avg `-0.0014` n `6`; index avg `0.1004` n `23`; metal avg `0.5301` n `18`; unknown avg `-0.1719` n `417`
- 4h: commodity avg `-0.1177` n `12`; crypto_alt avg `0.5809` n `228`; crypto_major avg `0.5103` n `8`; equity avg `0.016` n `69`; fx avg `-0.0011` n `6`; index avg `0.0258` n `23`; metal avg `0.2367` n `18`; unknown avg `0.3504` n `407`
- 24h: commodity avg `0.3911` n `12`; crypto_alt avg `1.5168` n `228`; crypto_major avg `2.0786` n `8`; equity avg `3.4329` n `69`; fx avg `0.1432` n `6`; index avg `1.2881` n `23`; metal avg `1.8881` n `18`; unknown avg `0.9642` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
