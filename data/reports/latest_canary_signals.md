# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T05:07:29.222968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `13`; crypto_alt avg `0.4698` n `238`; crypto_major avg `0.3624` n `8`; equity avg `0.2954` n `155`; fx avg `-0.0057` n `6`; index avg `0.0479` n `27`; metal avg `0.063` n `20`; unknown avg `1.46` n `1232`
- 1h: commodity avg `0.0018` n `13`; crypto_alt avg `1.0946` n `238`; crypto_major avg `1.0568` n `8`; equity avg `0.7717` n `155`; fx avg `0.0075` n `6`; index avg `0.1592` n `27`; metal avg `0.0854` n `20`; unknown avg `1.1475` n `1220`
- 4h: commodity avg `-0.0277` n `13`; crypto_alt avg `-1.4946` n `238`; crypto_major avg `-0.6413` n `8`; equity avg `-0.5185` n `155`; fx avg `0.0126` n `6`; index avg `-0.0433` n `27`; metal avg `-0.1685` n `20`; unknown avg `1.408` n `1198`
- 24h: commodity avg `-0.1049` n `13`; crypto_alt avg `-1.6346` n `238`; crypto_major avg `-0.8492` n `8`; equity avg `-0.6331` n `154`; fx avg `0.0054` n `6`; index avg `0.0361` n `27`; metal avg `-0.1262` n `20`; unknown avg `33.5288` n `976`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
