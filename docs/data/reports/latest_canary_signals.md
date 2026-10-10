# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T07:07:29.764400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `13`; crypto_alt avg `-0.1767` n `235`; crypto_major avg `-0.0166` n `8`; equity avg `-0.0162` n `150`; fx avg `-0.005` n `6`; index avg `0.0016` n `26`; metal avg `0.0065` n `20`; unknown avg `0.2283` n `1115`
- 1h: commodity avg `0.0083` n `13`; crypto_alt avg `-0.177` n `235`; crypto_major avg `-0.1005` n `8`; equity avg `-0.0398` n `150`; fx avg `-0.005` n `6`; index avg `-0.0184` n `26`; metal avg `0.0059` n `20`; unknown avg `1.7069` n `1114`
- 4h: commodity avg `0.0706` n `13`; crypto_alt avg `-0.0774` n `235`; crypto_major avg `0.0604` n `8`; equity avg `-0.0411` n `150`; fx avg `0.0006` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0086` n `20`; unknown avg `0.0769` n `1092`
- 24h: commodity avg `0.0026` n `13`; crypto_alt avg `1.5233` n `235`; crypto_major avg `0.0593` n `8`; equity avg `-0.2032` n `150`; fx avg `-0.0352` n `6`; index avg `-0.007` n `26`; metal avg `0.0191` n `20`; unknown avg `666.9329` n `904`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
