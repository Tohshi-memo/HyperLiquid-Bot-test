# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T06:37:28.095526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `13`; crypto_alt avg `-0.0199` n `235`; crypto_major avg `0.0064` n `8`; equity avg `0.0035` n `150`; fx avg `-0.0007` n `6`; index avg `-0.0026` n `26`; metal avg `0.0048` n `20`; unknown avg `-0.0004` n `1116`
- 1h: commodity avg `0.0164` n `13`; crypto_alt avg `-0.2727` n `235`; crypto_major avg `-0.1458` n `8`; equity avg `-0.0351` n `150`; fx avg `-0.0007` n `6`; index avg `-0.0062` n `26`; metal avg `0.0067` n `20`; unknown avg `-0.0026` n `1098`
- 4h: commodity avg `0.0714` n `13`; crypto_alt avg `0.0409` n `235`; crypto_major avg `0.0876` n `8`; equity avg `0.0047` n `150`; fx avg `0.0037` n `6`; index avg `0.0121` n `26`; metal avg `-0.006` n `20`; unknown avg `-0.1151` n `1092`
- 24h: commodity avg `-0.0117` n `13`; crypto_alt avg `1.5103` n `235`; crypto_major avg `0.0192` n `8`; equity avg `-0.1155` n `150`; fx avg `-0.0345` n `6`; index avg `0.0144` n `26`; metal avg `0.0623` n `20`; unknown avg `666.9459` n `904`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
