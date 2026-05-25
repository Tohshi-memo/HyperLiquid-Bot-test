# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T23:07:16.154470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1437` n `12`; crypto_alt avg `0.0002` n `228`; crypto_major avg `0.0624` n `8`; equity avg `-0.1004` n `67`; fx avg `-0.0017` n `6`; index avg `-0.0388` n `23`; metal avg `0.1134` n `18`; unknown avg `-0.0492` n `405`
- 1h: commodity avg `0.0363` n `12`; crypto_alt avg `-0.4689` n `228`; crypto_major avg `-0.2177` n `8`; equity avg `-0.205` n `67`; fx avg `0.0086` n `6`; index avg `-0.1288` n `23`; metal avg `0.1185` n `18`; unknown avg `0.3769` n `405`
- 4h: commodity avg `0.1066` n `12`; crypto_alt avg `-1.0392` n `228`; crypto_major avg `-0.5072` n `8`; equity avg `-0.1999` n `67`; fx avg `0.0324` n `6`; index avg `-0.1186` n `23`; metal avg `0.1289` n `18`; unknown avg `-0.4725` n `405`
- 24h: commodity avg `-0.2393` n `12`; crypto_alt avg `1.6394` n `228`; crypto_major avg `0.0535` n `8`; equity avg `0.8161` n `67`; fx avg `-0.0664` n `6`; index avg `0.5012` n `23`; metal avg `0.5383` n `18`; unknown avg `1.0815` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
