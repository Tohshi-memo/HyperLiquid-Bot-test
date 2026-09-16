# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T08:07:26.726401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0718` n `12`; crypto_alt avg `-0.3236` n `234`; crypto_major avg `-0.3357` n `8`; equity avg `-0.1721` n `137`; fx avg `0.0075` n `6`; index avg `-0.024` n `27`; metal avg `-0.0429` n `20`; unknown avg `0.8059` n `917`
- 1h: commodity avg `0.0873` n `12`; crypto_alt avg `-0.8469` n `234`; crypto_major avg `-0.7866` n `8`; equity avg `-0.2551` n `137`; fx avg `-0.0091` n `6`; index avg `-0.0414` n `27`; metal avg `-0.1143` n `20`; unknown avg `1.3172` n `917`
- 4h: commodity avg `-0.0174` n `12`; crypto_alt avg `-0.8682` n `234`; crypto_major avg `-0.7649` n `8`; equity avg `0.0083` n `137`; fx avg `-0.0266` n `6`; index avg `-0.0013` n `27`; metal avg `-0.0755` n `20`; unknown avg `6.3664` n `881`
- 24h: commodity avg `0.019` n `12`; crypto_alt avg `-3.03` n `234`; crypto_major avg `-2.8496` n `8`; equity avg `0.146` n `137`; fx avg `0.0682` n `6`; index avg `0.162` n `27`; metal avg `0.6394` n `20`; unknown avg `18889.2151` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
