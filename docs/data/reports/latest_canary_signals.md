# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T05:52:24.641028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.003` n `13`; crypto_alt avg `-0.1071` n `238`; crypto_major avg `-0.0209` n `8`; equity avg `-0.1122` n `154`; fx avg `-0.0103` n `6`; index avg `-0.0101` n `27`; metal avg `0.0006` n `20`; unknown avg `0.0113` n `1238`
- 1h: commodity avg `0.0198` n `13`; crypto_alt avg `-0.2074` n `238`; crypto_major avg `-0.1438` n `8`; equity avg `0.0334` n `154`; fx avg `-0.0655` n `6`; index avg `0.0355` n `27`; metal avg `-0.0061` n `20`; unknown avg `-0.1964` n `1234`
- 4h: commodity avg `0.0235` n `13`; crypto_alt avg `-0.2827` n `238`; crypto_major avg `-0.1024` n `8`; equity avg `0.1892` n `154`; fx avg `-0.0058` n `6`; index avg `-0.0083` n `27`; metal avg `-0.135` n `20`; unknown avg `0.2172` n `1214`
- 24h: commodity avg `0.0581` n `13`; crypto_alt avg `1.6985` n `237`; crypto_major avg `1.7985` n `8`; equity avg `3.4812` n `154`; fx avg `0.0676` n `6`; index avg `0.4878` n `27`; metal avg `0.2183` n `20`; unknown avg `15.6888` n `1016`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
