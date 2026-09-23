# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T18:52:43.153560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0452` n `12`; crypto_alt avg `0.3792` n `234`; crypto_major avg `0.38` n `8`; equity avg `0.0067` n `141`; fx avg `0.0081` n `6`; index avg `0.0011` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.9923` n `943`
- 1h: commodity avg `0.1511` n `12`; crypto_alt avg `-0.4525` n `234`; crypto_major avg `-0.0795` n `8`; equity avg `-0.0566` n `141`; fx avg `-0.0003` n `6`; index avg `-0.0144` n `26`; metal avg `-0.0035` n `20`; unknown avg `1.3461` n `941`
- 4h: commodity avg `0.1733` n `12`; crypto_alt avg `-1.2412` n `234`; crypto_major avg `-0.5895` n `8`; equity avg `-0.0907` n `141`; fx avg `-0.0102` n `6`; index avg `-0.0451` n `26`; metal avg `-0.0368` n `20`; unknown avg `1.5348` n `919`
- 24h: commodity avg `0.469` n `12`; crypto_alt avg `-2.7412` n `234`; crypto_major avg `-3.3628` n `8`; equity avg `-1.2395` n `140`; fx avg `-0.0149` n `6`; index avg `-0.3434` n `26`; metal avg `-0.7959` n `20`; unknown avg `13.3026` n `878`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.2271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2147`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
