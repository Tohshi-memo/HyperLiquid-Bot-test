# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T00:07:24.718279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0543` n `12`; crypto_alt avg `0.0673` n `234`; crypto_major avg `0.0176` n `8`; equity avg `-0.0107` n `137`; fx avg `-0.0021` n `6`; index avg `-0.0152` n `27`; metal avg `-0.0008` n `20`; unknown avg `0.2966` n `917`
- 1h: commodity avg `-0.0426` n `12`; crypto_alt avg `0.0302` n `234`; crypto_major avg `-0.1585` n `8`; equity avg `-0.0244` n `137`; fx avg `0.0247` n `6`; index avg `-0.0042` n `27`; metal avg `-0.0249` n `20`; unknown avg `-0.342` n `917`
- 4h: commodity avg `-0.09` n `12`; crypto_alt avg `-0.2938` n `234`; crypto_major avg `-0.2546` n `8`; equity avg `-0.106` n `137`; fx avg `0.0328` n `6`; index avg `0.0006` n `27`; metal avg `-0.0152` n `20`; unknown avg `0.2844` n `849`
- 24h: commodity avg `0.4214` n `12`; crypto_alt avg `-3.6669` n `234`; crypto_major avg `-3.9674` n `8`; equity avg `-1.316` n `137`; fx avg `0.2579` n `6`; index avg `-0.0938` n `27`; metal avg `0.2278` n `20`; unknown avg `0.9458` n `802`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
