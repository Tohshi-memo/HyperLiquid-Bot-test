# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T08:22:28.892363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `0.1233` n `234`; crypto_major avg `0.0355` n `8`; equity avg `-0.102` n `137`; fx avg `0.0304` n `6`; index avg `-0.0235` n `27`; metal avg `-0.0719` n `20`; unknown avg `1.9401` n `921`
- 1h: commodity avg `0.1375` n `12`; crypto_alt avg `0.071` n `234`; crypto_major avg `0.0518` n `8`; equity avg `-0.0082` n `137`; fx avg `0.0683` n `6`; index avg `-0.0428` n `27`; metal avg `-0.0043` n `20`; unknown avg `2.1934` n `919`
- 4h: commodity avg `-0.1177` n `12`; crypto_alt avg `1.0667` n `234`; crypto_major avg `0.5757` n `8`; equity avg `0.2809` n `137`; fx avg `0.077` n `6`; index avg `-0.0035` n `27`; metal avg `0.1263` n `20`; unknown avg `0.6008` n `891`
- 24h: commodity avg `-0.3916` n `12`; crypto_alt avg `3.652` n `234`; crypto_major avg `2.1598` n `8`; equity avg `1.288` n `137`; fx avg `0.1156` n `6`; index avg `0.0716` n `27`; metal avg `-0.0616` n `20`; unknown avg `0.6038` n `721`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
