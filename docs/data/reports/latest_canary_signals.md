# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T20:52:33.590059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.03` n `13`; crypto_alt avg `0.0252` n `237`; crypto_major avg `-0.0263` n `8`; equity avg `-0.229` n `151`; fx avg `-0.0042` n `6`; index avg `-0.0347` n `26`; metal avg `0.0005` n `20`; unknown avg `12.5426` n `1233`
- 1h: commodity avg `-0.012` n `13`; crypto_alt avg `-0.3563` n `237`; crypto_major avg `-0.366` n `8`; equity avg `-0.4636` n `151`; fx avg `-0.0193` n `6`; index avg `-0.0533` n `26`; metal avg `-0.0324` n `20`; unknown avg `9.2953` n `1173`
- 4h: commodity avg `0.1352` n `13`; crypto_alt avg `0.2127` n `237`; crypto_major avg `0.244` n `8`; equity avg `-0.431` n `151`; fx avg `-0.0294` n `6`; index avg `-0.0316` n `26`; metal avg `-0.0706` n `20`; unknown avg `2.4021` n `1173`
- 24h: commodity avg `0.5528` n `13`; crypto_alt avg `-5.6819` n `237`; crypto_major avg `-4.2487` n `8`; equity avg `-6.0241` n `151`; fx avg `-0.1878` n `6`; index avg `-0.7295` n `26`; metal avg `-1.0089` n `20`; unknown avg `60.652` n `934`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
