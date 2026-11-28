# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T13:07:24.043876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.73` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0106` n `13`; crypto_alt avg `-0.0123` n `239`; crypto_major avg `-0.0286` n `8`; equity avg `-0.0654` n `168`; fx avg `0.0007` n `6`; index avg `-0.0058` n `27`; metal avg `-0.0005` n `20`; unknown avg `3.3549` n `1251`
- 1h: commodity avg `0.0074` n `13`; crypto_alt avg `-0.1481` n `239`; crypto_major avg `-0.1832` n `8`; equity avg `-0.0696` n `168`; fx avg `-0.0197` n `6`; index avg `-0.0028` n `27`; metal avg `-0.0042` n `20`; unknown avg `3.1672` n `1253`
- 4h: commodity avg `-0.0067` n `13`; crypto_alt avg `-0.7113` n `239`; crypto_major avg `-0.369` n `8`; equity avg `-0.1298` n `168`; fx avg `-0.0234` n `6`; index avg `-0.0098` n `27`; metal avg `0.0209` n `20`; unknown avg `301.8889` n `1245`
- 24h: commodity avg `-0.3263` n `13`; crypto_alt avg `-3.5791` n `239`; crypto_major avg `-3.0955` n `8`; equity avg `-0.2246` n `168`; fx avg `-0.1014` n `6`; index avg `-0.0052` n `27`; metal avg `-0.0818` n `20`; unknown avg `190.5559` n `1092`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
