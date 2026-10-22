# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T21:07:33.972475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `13`; crypto_alt avg `0.2893` n `237`; crypto_major avg `0.2846` n `8`; equity avg `0.1628` n `151`; fx avg `-0.0087` n `6`; index avg `0.0125` n `26`; metal avg `0.0289` n `20`; unknown avg `7.4432` n `1225`
- 1h: commodity avg `-0.0239` n `13`; crypto_alt avg `-0.1318` n `237`; crypto_major avg `-0.0522` n `8`; equity avg `-0.4235` n `151`; fx avg `-0.0236` n `6`; index avg `-0.0712` n `26`; metal avg `-0.0069` n `20`; unknown avg `1.1788` n `1181`
- 4h: commodity avg `0.0792` n `13`; crypto_alt avg `0.0608` n `237`; crypto_major avg `0.2047` n `8`; equity avg `-0.2449` n `151`; fx avg `-0.0418` n `6`; index avg `-0.0303` n `26`; metal avg `-0.0594` n `20`; unknown avg `0.1894` n `1167`
- 24h: commodity avg `0.534` n `13`; crypto_alt avg `-5.4162` n `237`; crypto_major avg `-3.9796` n `8`; equity avg `-5.8815` n `151`; fx avg `-0.1964` n `6`; index avg `-0.7177` n `26`; metal avg `-0.981` n `20`; unknown avg `61.0386` n `934`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
