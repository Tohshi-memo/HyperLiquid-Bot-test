# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T08:52:31.184731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0279` n `13`; crypto_alt avg `-0.1936` n `238`; crypto_major avg `-0.2378` n `8`; equity avg `-0.1661` n `155`; fx avg `0.0002` n `6`; index avg `-0.0217` n `27`; metal avg `-0.1144` n `20`; unknown avg `1.7346` n `1238`
- 1h: commodity avg `-0.0545` n `13`; crypto_alt avg `0.1732` n `238`; crypto_major avg `0.1241` n `8`; equity avg `-0.0677` n `155`; fx avg `-0.0107` n `6`; index avg `-0.0267` n `27`; metal avg `-0.0702` n `20`; unknown avg `164.0279` n `1216`
- 4h: commodity avg `-0.0034` n `13`; crypto_alt avg `-0.6364` n `238`; crypto_major avg `-0.3641` n `8`; equity avg `-0.5088` n `155`; fx avg `0.0001` n `6`; index avg `-0.0615` n `27`; metal avg `-0.2324` n `20`; unknown avg `1.0214` n `1192`
- 24h: commodity avg `-0.0549` n `13`; crypto_alt avg `-2.9798` n `238`; crypto_major avg `-2.1697` n `8`; equity avg `-1.6596` n `154`; fx avg `0.0347` n `6`; index avg `-0.1192` n `27`; metal avg `-0.5058` n `20`; unknown avg `32.563` n `968`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
