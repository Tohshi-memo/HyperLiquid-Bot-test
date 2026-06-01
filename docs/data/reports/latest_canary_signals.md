# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T21:07:20.663895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.12` n `12`; crypto_alt avg `-0.3573` n `228`; crypto_major avg `-0.2164` n `8`; equity avg `0.029` n `69`; fx avg `-0.0011` n `6`; index avg `0.004` n `23`; metal avg `-0.0081` n `18`; unknown avg `0.5912` n `422`
- 1h: commodity avg `-0.0973` n `12`; crypto_alt avg `-0.4806` n `228`; crypto_major avg `-0.3353` n `8`; equity avg `0.0332` n `69`; fx avg `-0.0003` n `6`; index avg `-0.1055` n `23`; metal avg `-0.0835` n `18`; unknown avg `0.5379` n `422`
- 4h: commodity avg `-0.2954` n `12`; crypto_alt avg `-0.016` n `228`; crypto_major avg `0.2284` n `8`; equity avg `-0.4329` n `69`; fx avg `0.0193` n `6`; index avg `0.0755` n `23`; metal avg `0.0382` n `18`; unknown avg `-0.2524` n `422`
- 24h: commodity avg `0.5475` n `12`; crypto_alt avg `0.8341` n `228`; crypto_major avg `-0.8067` n `8`; equity avg `-0.1718` n `69`; fx avg `0.0669` n `6`; index avg `0.2196` n `23`; metal avg `-0.0765` n `18`; unknown avg `2.4348` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
