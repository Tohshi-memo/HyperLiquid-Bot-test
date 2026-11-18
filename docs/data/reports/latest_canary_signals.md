# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T21:07:32.332463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.057` n `13`; crypto_alt avg `0.1724` n `239`; crypto_major avg `0.1191` n `8`; equity avg `-0.0906` n `164`; fx avg `-0.001` n `6`; index avg `-0.0065` n `27`; metal avg `-0.031` n `20`; unknown avg `0.3695` n `1231`
- 1h: commodity avg `-0.0883` n `13`; crypto_alt avg `0.1012` n `239`; crypto_major avg `-0.0868` n `8`; equity avg `-0.0233` n `164`; fx avg `0.0036` n `6`; index avg `0.0066` n `27`; metal avg `0.0008` n `20`; unknown avg `0.55` n `1233`
- 4h: commodity avg `0.2737` n `13`; crypto_alt avg `0.0965` n `239`; crypto_major avg `-0.1211` n `8`; equity avg `0.0591` n `164`; fx avg `0.011` n `6`; index avg `-0.0027` n `27`; metal avg `-0.0081` n `20`; unknown avg `-0.2164` n `1225`
- 24h: commodity avg `-0.1803` n `13`; crypto_alt avg `-0.3764` n `239`; crypto_major avg `-1.2411` n `8`; equity avg `-0.3421` n `164`; fx avg `-0.1657` n `6`; index avg `-0.0109` n `27`; metal avg `-1.1094` n `20`; unknown avg `-0.2639` n `1126`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
