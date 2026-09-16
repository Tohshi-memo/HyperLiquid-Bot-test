# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T12:52:33.012160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.15` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.0161` n `234`; crypto_major avg `0.0636` n `8`; equity avg `0.0234` n `137`; fx avg `0.0125` n `6`; index avg `-0.0002` n `27`; metal avg `0.0224` n `20`; unknown avg `-0.0617` n `919`
- 1h: commodity avg `0.063` n `12`; crypto_alt avg `-0.5177` n `234`; crypto_major avg `-0.5345` n `8`; equity avg `-0.1031` n `137`; fx avg `0.0141` n `6`; index avg `-0.01` n `27`; metal avg `-0.0895` n `20`; unknown avg `0.3461` n `911`
- 4h: commodity avg `-0.004` n `12`; crypto_alt avg `0.5601` n `234`; crypto_major avg `0.6603` n `8`; equity avg `0.3595` n `137`; fx avg `-0.0163` n `6`; index avg `0.0616` n `27`; metal avg `0.0868` n `20`; unknown avg `0.6254` n `911`
- 24h: commodity avg `0.2878` n `12`; crypto_alt avg `-3.1535` n `234`; crypto_major avg `-2.9473` n `8`; equity avg `-0.1639` n `137`; fx avg `0.1001` n `6`; index avg `0.0448` n `27`; metal avg `0.3057` n `20`; unknown avg `18891.2149` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
