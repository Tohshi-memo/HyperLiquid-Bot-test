# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T01:37:23.350988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.51` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.9139` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0826` n `12`; crypto_alt avg `-0.2831` n `228`; crypto_major avg `-0.4941` n `8`; equity avg `-0.024` n `69`; fx avg `-0.0239` n `6`; index avg `-0.0437` n `23`; metal avg `-0.0243` n `18`; unknown avg `-0.2698` n `422`
- 1h: commodity avg `0.0479` n `12`; crypto_alt avg `-0.2997` n `228`; crypto_major avg `-0.8575` n `8`; equity avg `-0.0228` n `69`; fx avg `0.001` n `6`; index avg `-0.0491` n `23`; metal avg `-0.3923` n `18`; unknown avg `-0.7198` n `422`
- 4h: commodity avg `-0.0823` n `12`; crypto_alt avg `-1.6821` n `228`; crypto_major avg `-1.719` n `8`; equity avg `-0.2677` n `69`; fx avg `0.0036` n `6`; index avg `0.1949` n `23`; metal avg `-0.4791` n `18`; unknown avg `-1.1131` n `422`
- 24h: commodity avg `0.7181` n `12`; crypto_alt avg `-3.5503` n `228`; crypto_major avg `-5.4301` n `8`; equity avg `1.5781` n `69`; fx avg `0.0336` n `6`; index avg `1.3587` n `23`; metal avg `-0.4145` n `18`; unknown avg `-0.5628` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
