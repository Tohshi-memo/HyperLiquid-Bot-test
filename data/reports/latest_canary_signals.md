# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T21:37:27.498390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `13`; crypto_alt avg `-0.2454` n `237`; crypto_major avg `-0.2439` n `8`; equity avg `-0.1448` n `151`; fx avg `0.0045` n `6`; index avg `-0.0293` n `26`; metal avg `0.0092` n `20`; unknown avg `0.1153` n `1233`
- 1h: commodity avg `-0.0051` n `13`; crypto_alt avg `0.4246` n `237`; crypto_major avg `0.3636` n `8`; equity avg `-0.0298` n `151`; fx avg `0.0007` n `6`; index avg `-0.0392` n `26`; metal avg `0.0466` n `20`; unknown avg `10.3353` n `1225`
- 4h: commodity avg `-0.0446` n `13`; crypto_alt avg `-0.0623` n `237`; crypto_major avg `0.1972` n `8`; equity avg `-0.3527` n `151`; fx avg `-0.0347` n `6`; index avg `-0.1078` n `26`; metal avg `-0.0929` n `20`; unknown avg `-0.4769` n `1167`
- 24h: commodity avg `0.517` n `13`; crypto_alt avg `-5.3126` n `237`; crypto_major avg `-3.879` n `8`; equity avg `-5.8482` n `151`; fx avg `-0.183` n `6`; index avg `-0.7338` n `26`; metal avg `-0.9645` n `20`; unknown avg `60.3276` n `934`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
