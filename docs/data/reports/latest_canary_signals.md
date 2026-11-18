# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T08:22:28.180328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0254` n `13`; crypto_alt avg `-0.2173` n `239`; crypto_major avg `-0.1734` n `8`; equity avg `-0.0891` n `163`; fx avg `-0.0313` n `6`; index avg `-0.004` n `27`; metal avg `-0.1075` n `20`; unknown avg `1.0226` n `1262`
- 1h: commodity avg `0.1253` n `13`; crypto_alt avg `-0.1778` n `239`; crypto_major avg `-0.0944` n `8`; equity avg `0.0816` n `163`; fx avg `-0.0641` n `6`; index avg `0.0314` n `27`; metal avg `-0.2182` n `20`; unknown avg `0.1862` n `1244`
- 4h: commodity avg `-0.1463` n `13`; crypto_alt avg `0.3383` n `239`; crypto_major avg `0.4018` n `8`; equity avg `0.346` n `163`; fx avg `-0.0883` n `6`; index avg `0.0377` n `27`; metal avg `-0.3823` n `20`; unknown avg `0.8896` n `1212`
- 24h: commodity avg `-0.0868` n `13`; crypto_alt avg `0.3389` n `239`; crypto_major avg `0.8165` n `8`; equity avg `0.8236` n `163`; fx avg `-0.1679` n `6`; index avg `0.0566` n `27`; metal avg `-1.0896` n `20`; unknown avg `9.7568` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
