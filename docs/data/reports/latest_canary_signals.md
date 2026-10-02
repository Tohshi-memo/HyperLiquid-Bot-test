# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T12:52:28.553637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0951` n `13`; crypto_alt avg `0.001` n `234`; crypto_major avg `-0.225` n `8`; equity avg `-0.051` n `142`; fx avg `0.0209` n `6`; index avg `-0.0209` n `26`; metal avg `-0.1591` n `20`; unknown avg `5.2102` n `985`
- 1h: commodity avg `0.094` n `13`; crypto_alt avg `0.6023` n `234`; crypto_major avg `0.1967` n `8`; equity avg `0.6488` n `142`; fx avg `0.0026` n `6`; index avg `0.1661` n `26`; metal avg `0.1369` n `20`; unknown avg `3.6571` n `977`
- 4h: commodity avg `0.158` n `13`; crypto_alt avg `0.4627` n `234`; crypto_major avg `0.2575` n `8`; equity avg `0.2575` n `142`; fx avg `-0.0255` n `6`; index avg `0.1399` n `26`; metal avg `0.1` n `20`; unknown avg `0.0755` n `975`
- 24h: commodity avg `-0.529` n `13`; crypto_alt avg `2.6711` n `234`; crypto_major avg `2.3798` n `8`; equity avg `1.6458` n `142`; fx avg `-0.3318` n `6`; index avg `0.3538` n `26`; metal avg `0.0655` n `20`; unknown avg `0.3277` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
