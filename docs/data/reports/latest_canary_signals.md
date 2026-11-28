# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T11:52:24.402781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.47` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0017` n `13`; crypto_alt avg `-0.0482` n `239`; crypto_major avg `0.0186` n `8`; equity avg `-0.0099` n `168`; fx avg `-0.0017` n `6`; index avg `-0.002` n `27`; metal avg `0.0027` n `20`; unknown avg `0.3387` n `1269`
- 1h: commodity avg `-0.0173` n `13`; crypto_alt avg `-0.051` n `239`; crypto_major avg `0.1204` n `8`; equity avg `0.0377` n `168`; fx avg `0.0034` n `6`; index avg `-0.0028` n `27`; metal avg `0.0119` n `20`; unknown avg `5.2077` n `1261`
- 4h: commodity avg `-0.0499` n `13`; crypto_alt avg `-0.5236` n `239`; crypto_major avg `-0.6822` n `8`; equity avg `-0.2044` n `168`; fx avg `0.0044` n `6`; index avg `-0.0267` n `27`; metal avg `0.0221` n `20`; unknown avg `3.4058` n `1215`
- 24h: commodity avg `-0.5752` n `13`; crypto_alt avg `-3.3776` n `239`; crypto_major avg `-3.2095` n `8`; equity avg `0.1506` n `168`; fx avg `-0.0759` n `6`; index avg `0.0636` n `27`; metal avg `-0.1601` n `20`; unknown avg `190.1385` n `1089`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
