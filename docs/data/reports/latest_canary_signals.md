# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T02:22:37.951015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `0.3238` n `239`; crypto_major avg `0.2976` n `8`; equity avg `0.3331` n `168`; fx avg `0.0147` n `6`; index avg `0.0206` n `27`; metal avg `0.1174` n `20`; unknown avg `0.0162` n `1265`
- 1h: commodity avg `-0.0791` n `13`; crypto_alt avg `0.4623` n `239`; crypto_major avg `0.4342` n `8`; equity avg `-0.0215` n `168`; fx avg `-0.0253` n `6`; index avg `-0.0272` n `27`; metal avg `0.0676` n `20`; unknown avg `375.3404` n `1261`
- 4h: commodity avg `-0.0034` n `13`; crypto_alt avg `1.578` n `239`; crypto_major avg `1.264` n `8`; equity avg `1.6646` n `168`; fx avg `-0.0516` n `6`; index avg `0.1462` n `27`; metal avg `0.1598` n `20`; unknown avg `66.4705` n `1199`
- 24h: commodity avg `0.5828` n `13`; crypto_alt avg `4.6243` n `239`; crypto_major avg `3.5969` n `8`; equity avg `2.4374` n `168`; fx avg `-0.035` n `6`; index avg `0.2445` n `27`; metal avg `0.3192` n `20`; unknown avg `769.0917` n `1019`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1947`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
