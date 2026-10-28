# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T06:07:40.608912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.58` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0023` n `13`; crypto_alt avg `0.0474` n `238`; crypto_major avg `0.0363` n `8`; equity avg `0.1409` n `154`; fx avg `-0.0077` n `6`; index avg `0.0206` n `27`; metal avg `-0.0088` n `20`; unknown avg `3.3865` n `1216`
- 1h: commodity avg `0.0246` n `13`; crypto_alt avg `-0.0269` n `238`; crypto_major avg `0.0254` n `8`; equity avg `0.1356` n `154`; fx avg `-0.0487` n `6`; index avg `0.043` n `27`; metal avg `0.0028` n `20`; unknown avg `2.7934` n `1216`
- 4h: commodity avg `0.0052` n `13`; crypto_alt avg `-0.2628` n `238`; crypto_major avg `0.0294` n `8`; equity avg `0.4765` n `154`; fx avg `-0.008` n `6`; index avg `0.0252` n `27`; metal avg `-0.0906` n `20`; unknown avg `0.6222` n `1198`
- 24h: commodity avg `0.001` n `13`; crypto_alt avg `1.8341` n `237`; crypto_major avg `1.9314` n `8`; equity avg `3.6469` n `154`; fx avg `0.0529` n `6`; index avg `0.4957` n `27`; metal avg `0.228` n `20`; unknown avg `16.1393` n `1016`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
