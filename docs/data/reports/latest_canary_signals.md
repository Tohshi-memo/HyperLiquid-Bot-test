# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T09:52:28.712013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0249` n `12`; crypto_alt avg `0.0927` n `234`; crypto_major avg `0.0354` n `8`; equity avg `0.0465` n `137`; fx avg `-0.0136` n `6`; index avg `0.0115` n `27`; metal avg `0.0063` n `20`; unknown avg `-0.2002` n `919`
- 1h: commodity avg `-0.0048` n `12`; crypto_alt avg `0.5535` n `234`; crypto_major avg `0.5066` n `8`; equity avg `0.1962` n `137`; fx avg `-0.0019` n `6`; index avg `0.0176` n `27`; metal avg `0.0385` n `20`; unknown avg `-0.0936` n `917`
- 4h: commodity avg `-0.059` n `12`; crypto_alt avg `-0.146` n `234`; crypto_major avg `0.0183` n `8`; equity avg `0.24` n `137`; fx avg `-0.0435` n `6`; index avg `0.0544` n `27`; metal avg `-0.0672` n `20`; unknown avg `5.948` n `881`
- 24h: commodity avg `0.0337` n `12`; crypto_alt avg `-3.0376` n `234`; crypto_major avg `-2.8285` n `8`; equity avg `0.0681` n `137`; fx avg `0.0857` n `6`; index avg `0.1138` n `27`; metal avg `0.5115` n `20`; unknown avg `18892.7602` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
