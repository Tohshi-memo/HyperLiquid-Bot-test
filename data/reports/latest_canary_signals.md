# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T06:22:24.291792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.1277` n `228`; crypto_major avg `-0.1492` n `8`; equity avg `-0.0055` n `65`; fx avg `0.0015` n `5`; index avg `0.0107` n `23`; metal avg `-0.0032` n `18`; unknown avg `-0.325` n `376`
- 1h: commodity avg `0.0279` n `12`; crypto_alt avg `0.0722` n `228`; crypto_major avg `-0.0416` n `8`; equity avg `0.0058` n `65`; fx avg `0.0193` n `5`; index avg `-0.0057` n `23`; metal avg `0.0029` n `18`; unknown avg `-0.0152` n `356`
- 4h: commodity avg `0.0983` n `12`; crypto_alt avg `-0.015` n `228`; crypto_major avg `-0.0365` n `8`; equity avg `0.0267` n `65`; fx avg `-0.0066` n `5`; index avg `0.0356` n `23`; metal avg `0.0033` n `18`; unknown avg `-0.0527` n `355`
- 24h: commodity avg `0.0738` n `12`; crypto_alt avg `4.7175` n `228`; crypto_major avg `2.9455` n `8`; equity avg `3.3988` n `65`; fx avg `-0.005` n `5`; index avg `1.2749` n `23`; metal avg `-0.2748` n `18`; unknown avg `1.3576` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
