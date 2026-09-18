# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T08:22:32.598385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0352` n `12`; crypto_alt avg `0.0392` n `234`; crypto_major avg `0.2249` n `8`; equity avg `0.0946` n `140`; fx avg `0.0134` n `6`; index avg `0.0011` n `26`; metal avg `-0.0258` n `20`; unknown avg `1.7731` n `927`
- 1h: commodity avg `0.1096` n `12`; crypto_alt avg `0.2177` n `234`; crypto_major avg `0.1879` n `8`; equity avg `0.0655` n `140`; fx avg `0.0954` n `6`; index avg `0.0054` n `26`; metal avg `0.0397` n `20`; unknown avg `1.5097` n `925`
- 4h: commodity avg `-0.1635` n `12`; crypto_alt avg `0.5723` n `234`; crypto_major avg `0.8849` n `8`; equity avg `0.604` n `140`; fx avg `0.0588` n `6`; index avg `0.1032` n `26`; metal avg `0.3577` n `20`; unknown avg `0.1067` n `863`
- 24h: commodity avg `-0.3449` n `12`; crypto_alt avg `5.1402` n `234`; crypto_major avg `3.9125` n `8`; equity avg `2.2637` n `140`; fx avg `0.1651` n `6`; index avg `0.3732` n `26`; metal avg `0.682` n `20`; unknown avg `2.5442` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
