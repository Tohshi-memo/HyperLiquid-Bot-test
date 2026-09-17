# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T01:22:29.249213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1519` n `12`; crypto_alt avg `-0.0911` n `234`; crypto_major avg `0.0605` n `8`; equity avg `-0.0265` n `137`; fx avg `0.0007` n `6`; index avg `-0.0049` n `27`; metal avg `0.0072` n `20`; unknown avg `-0.0351` n `919`
- 1h: commodity avg `0.1149` n `12`; crypto_alt avg `-0.1555` n `234`; crypto_major avg `-0.085` n `8`; equity avg `0.0721` n `137`; fx avg `0.0322` n `6`; index avg `0.0295` n `27`; metal avg `0.1594` n `20`; unknown avg `0.7033` n `911`
- 4h: commodity avg `0.0223` n `12`; crypto_alt avg `1.0928` n `234`; crypto_major avg `0.3696` n `8`; equity avg `0.7765` n `137`; fx avg `0.0076` n `6`; index avg `0.1705` n `27`; metal avg `0.31` n `20`; unknown avg `0.9075` n `813`
- 24h: commodity avg `-0.5083` n `12`; crypto_alt avg `1.5226` n `234`; crypto_major avg `0.9646` n `8`; equity avg `1.6671` n `137`; fx avg `-0.0251` n `6`; index avg `0.1839` n `27`; metal avg `0.0132` n `20`; unknown avg `0.9672` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
