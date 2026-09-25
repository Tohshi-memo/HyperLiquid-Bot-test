# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T21:07:29.523108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `-0.6249` n `234`; crypto_major avg `-0.4691` n `8`; equity avg `-0.0436` n `141`; fx avg `-0.0067` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0187` n `20`; unknown avg `-0.2983` n `956`
- 1h: commodity avg `-0.0013` n `12`; crypto_alt avg `-0.394` n `234`; crypto_major avg `-0.4386` n `8`; equity avg `0.005` n `141`; fx avg `-0.0131` n `6`; index avg `-0.001` n `26`; metal avg `-0.0095` n `20`; unknown avg `0.6448` n `904`
- 4h: commodity avg `0.2417` n `12`; crypto_alt avg `0.1016` n `234`; crypto_major avg `-0.2806` n `8`; equity avg `-0.2168` n `141`; fx avg `-0.0188` n `6`; index avg `0.0172` n `26`; metal avg `-0.0187` n `20`; unknown avg `0.0525` n `876`
- 24h: commodity avg `-0.6695` n `12`; crypto_alt avg `1.9158` n `234`; crypto_major avg `0.4` n `8`; equity avg `0.0941` n `141`; fx avg `-0.2498` n `6`; index avg `0.2425` n `26`; metal avg `0.1637` n `20`; unknown avg `1148.1536` n `794`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
