# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T22:47:57.082259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0021` n `13`; crypto_alt avg `-0.0644` n `239`; crypto_major avg `-0.278` n `8`; equity avg `0.0712` n `166`; fx avg `-0.003` n `6`; index avg `0.0182` n `27`; metal avg `0.0101` n `20`; unknown avg `2.8829` n `1260`
- 1h: commodity avg `0.0092` n `13`; crypto_alt avg `0.2247` n `239`; crypto_major avg `-0.0233` n `8`; equity avg `0.3843` n `166`; fx avg `-0.0119` n `6`; index avg `0.0446` n `27`; metal avg `0.019` n `20`; unknown avg `160.4406` n `1242`
- 4h: commodity avg `0.3253` n `13`; crypto_alt avg `0.4688` n `239`; crypto_major avg `0.1575` n `8`; equity avg `-0.3103` n `166`; fx avg `-0.0382` n `6`; index avg `-0.1125` n `27`; metal avg `0.0825` n `20`; unknown avg `2.2428` n `1208`
- 24h: commodity avg `0.2786` n `13`; crypto_alt avg `-4.9981` n `239`; crypto_major avg `-5.8084` n `8`; equity avg `-6.269` n `166`; fx avg `0.0098` n `6`; index avg `-0.7064` n `27`; metal avg `-0.8281` n `20`; unknown avg `31.8382` n `1131`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
