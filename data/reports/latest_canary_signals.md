# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T17:22:34.297201+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `-0.0581` n `234`; crypto_major avg `-0.1878` n `8`; equity avg `-0.014` n `140`; fx avg `0.0005` n `6`; index avg `0.0009` n `26`; metal avg `-0.0081` n `20`; unknown avg `0.3285` n `935`
- 1h: commodity avg `0.0445` n `12`; crypto_alt avg `0.4141` n `234`; crypto_major avg `0.1251` n `8`; equity avg `0.0201` n `140`; fx avg `0.0016` n `6`; index avg `0.0011` n `26`; metal avg `-0.0087` n `20`; unknown avg `17.8439` n `899`
- 4h: commodity avg `-0.133` n `12`; crypto_alt avg `0.6918` n `234`; crypto_major avg `0.289` n `8`; equity avg `0.0675` n `140`; fx avg `-0.002` n `6`; index avg `0.0157` n `26`; metal avg `-0.0042` n `20`; unknown avg `5.6923` n `880`
- 24h: commodity avg `-0.0368` n `12`; crypto_alt avg `3.0971` n `234`; crypto_major avg `1.5907` n `8`; equity avg `0.6409` n `140`; fx avg `0.0238` n `6`; index avg `0.144` n `26`; metal avg `-0.0964` n `20`; unknown avg `3.8293` n `774`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
