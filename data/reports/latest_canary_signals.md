# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T06:52:15.499453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `-0.0814` n `228`; crypto_major avg `0.062` n `8`; equity avg `0.0169` n `65`; fx avg `0.0` n `5`; index avg `0.0054` n `23`; metal avg `-0.0001` n `18`; unknown avg `0.0312` n `376`
- 1h: commodity avg `0.036` n `12`; crypto_alt avg `-0.347` n `228`; crypto_major avg `-0.0839` n `8`; equity avg `0.0346` n `65`; fx avg `-0.0002` n `5`; index avg `0.0257` n `23`; metal avg `0.0027` n `18`; unknown avg `-0.1366` n `356`
- 4h: commodity avg `0.0952` n `12`; crypto_alt avg `-0.222` n `228`; crypto_major avg `-0.0609` n `8`; equity avg `0.0082` n `65`; fx avg `0.0183` n `5`; index avg `0.0081` n `23`; metal avg `-0.088` n `18`; unknown avg `-0.2572` n `355`
- 24h: commodity avg `0.0326` n `12`; crypto_alt avg `4.4323` n `228`; crypto_major avg `2.8703` n `8`; equity avg `3.3624` n `65`; fx avg `0.008` n `5`; index avg `1.2592` n `23`; metal avg `-0.2841` n `18`; unknown avg `1.3007` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
