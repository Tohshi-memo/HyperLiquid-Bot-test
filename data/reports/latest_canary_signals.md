# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T11:07:30.331201+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0314` n `13`; crypto_alt avg `-0.1567` n `239`; crypto_major avg `-0.1273` n `8`; equity avg `-0.1235` n `161`; fx avg `-0.0305` n `6`; index avg `-0.0078` n `27`; metal avg `-0.034` n `20`; unknown avg `159.1366` n `1257`
- 1h: commodity avg `0.0206` n `13`; crypto_alt avg `0.182` n `239`; crypto_major avg `0.3154` n `8`; equity avg `0.1702` n `161`; fx avg `0.006` n `6`; index avg `0.0142` n `27`; metal avg `-0.056` n `20`; unknown avg `0.4448` n `1253`
- 4h: commodity avg `0.3173` n `13`; crypto_alt avg `0.6964` n `239`; crypto_major avg `0.7394` n `8`; equity avg `0.7363` n `161`; fx avg `-0.0242` n `6`; index avg `0.016` n `27`; metal avg `0.0467` n `20`; unknown avg `41.1103` n `1223`
- 24h: commodity avg `0.7013` n `13`; crypto_alt avg `-0.4759` n `239`; crypto_major avg `-1.1002` n `8`; equity avg `2.8509` n `161`; fx avg `-0.2226` n `6`; index avg `0.2587` n `27`; metal avg `0.3036` n `20`; unknown avg `1.3188` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
