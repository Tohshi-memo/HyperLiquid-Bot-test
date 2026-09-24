# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T04:07:25.804695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0235` n `12`; crypto_alt avg `0.2311` n `234`; crypto_major avg `0.0495` n `8`; equity avg `-0.1812` n `141`; fx avg `0.0012` n `6`; index avg `-0.0248` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.1157` n `937`
- 1h: commodity avg `0.028` n `12`; crypto_alt avg `-0.4326` n `234`; crypto_major avg `-0.5217` n `8`; equity avg `-0.35` n `141`; fx avg `-0.0017` n `6`; index avg `-0.0425` n `26`; metal avg `-0.0189` n `20`; unknown avg `-0.1386` n `937`
- 4h: commodity avg `-0.0681` n `12`; crypto_alt avg `0.3982` n `234`; crypto_major avg `-0.6022` n `8`; equity avg `-0.4959` n `141`; fx avg `0.0338` n `6`; index avg `-0.0583` n `26`; metal avg `-0.0304` n `20`; unknown avg `3.3105` n `937`
- 24h: commodity avg `0.5411` n `12`; crypto_alt avg `-4.6718` n `234`; crypto_major avg `-4.6652` n `8`; equity avg `-1.9647` n `140`; fx avg `0.097` n `6`; index avg `-0.3741` n `26`; metal avg `-0.6743` n `20`; unknown avg `585.1644` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
