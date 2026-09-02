# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T06:37:25.134263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `0.0309` n `232`; crypto_major avg `-0.0118` n `8`; equity avg `-0.0254` n `132`; fx avg `-0.007` n `6`; index avg `-0.008` n `26`; metal avg `-0.0277` n `20`; unknown avg `0.0378` n `790`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `-0.3638` n `232`; crypto_major avg `-0.2758` n `8`; equity avg `-0.2051` n `132`; fx avg `-0.0439` n `6`; index avg `-0.0569` n `26`; metal avg `-0.0352` n `20`; unknown avg `0.0036` n `770`
- 4h: commodity avg `-0.0077` n `12`; crypto_alt avg `0.3754` n `232`; crypto_major avg `0.2749` n `8`; equity avg `-0.0613` n `132`; fx avg `-0.0999` n `6`; index avg `-0.0654` n `26`; metal avg `0.0678` n `20`; unknown avg `0.1009` n `770`
- 24h: commodity avg `0.8875` n `12`; crypto_alt avg `-1.0002` n `232`; crypto_major avg `-1.9441` n `8`; equity avg `-2.6493` n `130`; fx avg `-0.1584` n `6`; index avg `-0.5058` n `26`; metal avg `-0.9634` n `20`; unknown avg `-0.1499` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0448`, n `668`, weak_sample_signal
