# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T13:22:26.387563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0386` n `13`; crypto_alt avg `0.0463` n `239`; crypto_major avg `0.1145` n `8`; equity avg `-0.0637` n `168`; fx avg `-0.022` n `6`; index avg `-0.0015` n `27`; metal avg `-0.252` n `20`; unknown avg `0.5116` n `1262`
- 1h: commodity avg `-0.1821` n `13`; crypto_alt avg `-0.0219` n `239`; crypto_major avg `-0.0507` n `8`; equity avg `0.1037` n `168`; fx avg `-0.0431` n `6`; index avg `0.0262` n `27`; metal avg `-0.2824` n `20`; unknown avg `0.5977` n `1257`
- 4h: commodity avg `-0.3144` n `13`; crypto_alt avg `-0.0637` n `239`; crypto_major avg `-0.0373` n `8`; equity avg `-0.8125` n `168`; fx avg `0.0054` n `6`; index avg `-0.0315` n `27`; metal avg `-0.5028` n `20`; unknown avg `186.4427` n `1251`
- 24h: commodity avg `-0.1823` n `13`; crypto_alt avg `1.8143` n `239`; crypto_major avg `2.5078` n `8`; equity avg `3.2346` n `168`; fx avg `-0.1083` n `6`; index avg `0.2821` n `27`; metal avg `0.8232` n `20`; unknown avg `266.6391` n `1029`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
