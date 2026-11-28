# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T14:52:44.158051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.41` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.022` n `13`; crypto_alt avg `-0.0473` n `239`; crypto_major avg `0.053` n `8`; equity avg `0.0165` n `168`; fx avg `0.0084` n `6`; index avg `0.0006` n `27`; metal avg `0.0045` n `20`; unknown avg `3.398` n `1265`
- 1h: commodity avg `-0.0201` n `13`; crypto_alt avg `0.2142` n `239`; crypto_major avg `0.4933` n `8`; equity avg `0.1217` n `168`; fx avg `0.0101` n `6`; index avg `0.0093` n `27`; metal avg `0.0328` n `20`; unknown avg `4.2398` n `1253`
- 4h: commodity avg `-0.0131` n `13`; crypto_alt avg `-0.4176` n `239`; crypto_major avg `0.1532` n `8`; equity avg `-0.0885` n `168`; fx avg `0.0054` n `6`; index avg `-0.0052` n `27`; metal avg `-0.0031` n `20`; unknown avg `9.4329` n `1245`
- 24h: commodity avg `-0.3192` n `13`; crypto_alt avg `-1.8085` n `239`; crypto_major avg `-0.4083` n `8`; equity avg `1.8644` n `168`; fx avg `-0.0721` n `6`; index avg `0.1992` n `27`; metal avg `0.1691` n `20`; unknown avg `192.6895` n `1092`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
