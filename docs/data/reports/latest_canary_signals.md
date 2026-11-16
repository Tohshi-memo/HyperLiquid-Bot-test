# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T14:07:30.345723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.03` n `13`; crypto_alt avg `0.0273` n `239`; crypto_major avg `-0.0979` n `8`; equity avg `0.1384` n `162`; fx avg `0.0131` n `6`; index avg `0.0268` n `27`; metal avg `-0.0119` n `20`; unknown avg `0.2537` n `1259`
- 1h: commodity avg `-0.146` n `13`; crypto_alt avg `0.2514` n `239`; crypto_major avg `-0.075` n `8`; equity avg `-0.1443` n `162`; fx avg `0.0117` n `6`; index avg `-0.0128` n `27`; metal avg `-0.1096` n `20`; unknown avg `171.3123` n `1259`
- 4h: commodity avg `-0.3261` n `13`; crypto_alt avg `-0.2033` n `239`; crypto_major avg `-0.269` n `8`; equity avg `-0.5081` n `162`; fx avg `0.0287` n `6`; index avg `-0.0458` n `27`; metal avg `0.0543` n `20`; unknown avg `12.5071` n `1251`
- 24h: commodity avg `-0.5831` n `13`; crypto_alt avg `-1.1448` n `239`; crypto_major avg `-1.3872` n `8`; equity avg `-1.4447` n `162`; fx avg `-0.0121` n `6`; index avg `-0.1069` n `27`; metal avg `-0.0275` n `20`; unknown avg `237.6691` n `1054`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1373`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1154`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1087`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1053`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1039`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.084`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0762`, n `669`, weak_sample_signal
