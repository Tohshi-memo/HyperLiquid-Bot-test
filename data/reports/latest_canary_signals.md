# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T10:52:29.676933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `12`; crypto_alt avg `-0.0296` n `234`; crypto_major avg `-0.0814` n `8`; equity avg `-0.0121` n `141`; fx avg `0.0027` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.2679` n `962`
- 1h: commodity avg `0.0021` n `12`; crypto_alt avg `-0.0488` n `234`; crypto_major avg `-0.1768` n `8`; equity avg `-0.0263` n `141`; fx avg `-0.009` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0059` n `20`; unknown avg `0.6348` n `960`
- 4h: commodity avg `-0.0176` n `12`; crypto_alt avg `0.6777` n `234`; crypto_major avg `0.6194` n `8`; equity avg `0.1202` n `141`; fx avg `-0.0213` n `6`; index avg `0.0228` n `26`; metal avg `0.0045` n `20`; unknown avg `3.883` n `943`
- 24h: commodity avg `0.0595` n `12`; crypto_alt avg `0.8069` n `234`; crypto_major avg `0.6104` n `8`; equity avg `0.3692` n `141`; fx avg `-0.0148` n `6`; index avg `0.0352` n `26`; metal avg `-0.0031` n `20`; unknown avg `5.4847` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
