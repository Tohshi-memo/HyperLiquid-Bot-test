# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T01:22:28.563597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `13`; crypto_alt avg `0.1311` n `237`; crypto_major avg `0.1162` n `8`; equity avg `-0.0919` n `151`; fx avg `0.0081` n `6`; index avg `-0.0277` n `26`; metal avg `0.0066` n `20`; unknown avg `0.095` n `1233`
- 1h: commodity avg `0.0967` n `13`; crypto_alt avg `0.1895` n `237`; crypto_major avg `0.2189` n `8`; equity avg `0.6635` n `151`; fx avg `-0.0226` n `6`; index avg `0.0662` n `26`; metal avg `-0.0256` n `20`; unknown avg `0.6577` n `1231`
- 4h: commodity avg `0.0987` n `13`; crypto_alt avg `-0.0996` n `237`; crypto_major avg `-0.1214` n `8`; equity avg `0.2181` n `151`; fx avg `-0.0719` n `6`; index avg `0.0073` n `26`; metal avg `-0.0819` n `20`; unknown avg `0.1938` n `1185`
- 24h: commodity avg `0.4586` n `13`; crypto_alt avg `-4.5683` n `237`; crypto_major avg `-3.0399` n `8`; equity avg `-4.4014` n `151`; fx avg `-0.2341` n `6`; index avg `-0.5174` n `26`; metal avg `-0.8225` n `20`; unknown avg `53.879` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
