# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T06:52:31.315069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0154` n `13`; crypto_alt avg `0.0936` n `235`; crypto_major avg `-0.0453` n `8`; equity avg `-0.0208` n `150`; fx avg `0.0007` n `6`; index avg `-0.0169` n `26`; metal avg `-0.004` n `20`; unknown avg `1.5111` n `1117`
- 1h: commodity avg `0.0249` n `13`; crypto_alt avg `-0.1736` n `235`; crypto_major avg `-0.1802` n `8`; equity avg `-0.0554` n `150`; fx avg `0.0` n `6`; index avg `-0.0215` n `26`; metal avg `-0.003` n `20`; unknown avg `0.0347` n `1098`
- 4h: commodity avg `0.098` n `13`; crypto_alt avg `0.1609` n `235`; crypto_major avg `0.0418` n `8`; equity avg `-0.0221` n `150`; fx avg `0.0056` n `6`; index avg `-0.009` n `26`; metal avg `-0.0084` n `20`; unknown avg `-0.0222` n `1092`
- 24h: commodity avg `0.0091` n `13`; crypto_alt avg `1.5449` n `235`; crypto_major avg `-0.0301` n `8`; equity avg `-0.1388` n `150`; fx avg `-0.0231` n `6`; index avg `-0.0058` n `26`; metal avg `0.0416` n `20`; unknown avg `666.811` n `904`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
