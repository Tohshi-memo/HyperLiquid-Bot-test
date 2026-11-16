# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T00:52:25.743534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `0.1457` n `239`; crypto_major avg `0.0789` n `8`; equity avg `0.0766` n `162`; fx avg `0.0048` n `6`; index avg `-0.0014` n `27`; metal avg `0.046` n `20`; unknown avg `0.1597` n `1263`
- 1h: commodity avg `0.0235` n `13`; crypto_alt avg `-0.5127` n `239`; crypto_major avg `-0.679` n `8`; equity avg `-0.2318` n `162`; fx avg `-0.0235` n `6`; index avg `-0.0807` n `27`; metal avg `-0.0743` n `20`; unknown avg `0.6283` n `1255`
- 4h: commodity avg `-0.2719` n `13`; crypto_alt avg `-0.1657` n `239`; crypto_major avg `-0.1405` n `8`; equity avg `0.929` n `162`; fx avg `-0.0317` n `6`; index avg `0.1284` n `27`; metal avg `0.2862` n `20`; unknown avg `0.0882` n `1185`
- 24h: commodity avg `-0.2984` n `13`; crypto_alt avg `2.4261` n `239`; crypto_major avg `3.4828` n `8`; equity avg `2.077` n `162`; fx avg `0.0003` n `6`; index avg `0.2406` n `27`; metal avg `0.6041` n `20`; unknown avg `2.1213` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
