# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T15:37:31.543009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.41` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0586` n `13`; crypto_alt avg `-0.2334` n `239`; crypto_major avg `-0.1437` n `8`; equity avg `-0.7144` n `164`; fx avg `-0.0077` n `6`; index avg `-0.0749` n `27`; metal avg `-0.032` n `20`; unknown avg `2.7397` n `1265`
- 1h: commodity avg `-0.0332` n `13`; crypto_alt avg `-0.2223` n `239`; crypto_major avg `-0.1015` n `8`; equity avg `0.245` n `164`; fx avg `-0.0166` n `6`; index avg `-0.0076` n `27`; metal avg `-0.0906` n `20`; unknown avg `5.1639` n `1263`
- 4h: commodity avg `-0.0632` n `13`; crypto_alt avg `-0.7819` n `239`; crypto_major avg `-1.1206` n `8`; equity avg `-1.9317` n `164`; fx avg `-0.0221` n `6`; index avg `-0.1851` n `27`; metal avg `-0.1946` n `20`; unknown avg `2.1415` n `1257`
- 24h: commodity avg `-0.1837` n `13`; crypto_alt avg `-0.3169` n `239`; crypto_major avg `-0.705` n `8`; equity avg `0.2036` n `164`; fx avg `-0.1541` n `6`; index avg `0.0231` n `27`; metal avg `-1.2392` n `20`; unknown avg `0.7417` n `1136`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
