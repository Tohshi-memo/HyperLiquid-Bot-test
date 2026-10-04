# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T00:22:25.003070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `13`; crypto_alt avg `0.1535` n `235`; crypto_major avg `0.1337` n `8`; equity avg `0.0205` n `143`; fx avg `0.0022` n `6`; index avg `0.0002` n `26`; metal avg `0.002` n `20`; unknown avg `-0.1133` n `1079`
- 1h: commodity avg `-0.0605` n `13`; crypto_alt avg `0.0855` n `235`; crypto_major avg `0.0933` n `8`; equity avg `-0.0089` n `143`; fx avg `0.0034` n `6`; index avg `-0.001` n `26`; metal avg `-0.0028` n `20`; unknown avg `-0.0171` n `1071`
- 4h: commodity avg `0.0165` n `13`; crypto_alt avg `0.4256` n `235`; crypto_major avg `0.0275` n `8`; equity avg `0.0637` n `143`; fx avg `0.0064` n `6`; index avg `0.0006` n `26`; metal avg `0.0019` n `20`; unknown avg `-0.2525` n `1055`
- 24h: commodity avg `-0.0882` n `13`; crypto_alt avg `1.6304` n `235`; crypto_major avg `0.5687` n `8`; equity avg `0.1694` n `143`; fx avg `-0.012` n `6`; index avg `0.0352` n `26`; metal avg `-0.0142` n `20`; unknown avg `-0.0234` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1988`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
