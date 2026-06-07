# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T19:51:31.510179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.2126` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1173` n `12`; crypto_alt avg `-0.0645` n `228`; crypto_major avg `-0.0629` n `8`; equity avg `-0.0687` n `74`; fx avg `0.0034` n `6`; index avg `-0.1039` n `23`; metal avg `-0.0086` n `18`; unknown avg `-0.0879` n `516`
- 1h: commodity avg `0.416` n `12`; crypto_alt avg `-1.6227` n `228`; crypto_major avg `-1.3578` n `8`; equity avg `-0.6281` n `74`; fx avg `0.0202` n `6`; index avg `-0.1452` n `23`; metal avg `-0.2061` n `18`; unknown avg `-0.1875` n `516`
- 4h: commodity avg `0.6273` n `12`; crypto_alt avg `-1.8451` n `228`; crypto_major avg `-1.0158` n `8`; equity avg `-0.7154` n `74`; fx avg `0.0455` n `6`; index avg `-0.361` n `23`; metal avg `-0.1996` n `18`; unknown avg `-2.8155` n `516`
- 24h: commodity avg `0.6338` n `12`; crypto_alt avg `1.149` n `228`; crypto_major avg `2.5878` n `8`; equity avg `0.9948` n `74`; fx avg `-0.0486` n `6`; index avg `0.1646` n `23`; metal avg `0.3208` n `18`; unknown avg `-5.0003` n `505`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
