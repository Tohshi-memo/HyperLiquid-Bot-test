# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T04:22:14.222273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0482` n `12`; crypto_alt avg `-0.0447` n `228`; crypto_major avg `-0.2208` n `8`; equity avg `0.0008` n `65`; fx avg `0.0` n `5`; index avg `-0.0048` n `23`; metal avg `-0.017` n `18`; unknown avg `-0.0439` n `375`
- 1h: commodity avg `0.0979` n `12`; crypto_alt avg `-0.1307` n `228`; crypto_major avg `-0.0006` n `8`; equity avg `-0.0427` n `65`; fx avg `0.0008` n `5`; index avg `0.0544` n `23`; metal avg `-0.0648` n `18`; unknown avg `-0.4249` n `375`
- 4h: commodity avg `0.1929` n `12`; crypto_alt avg `0.8952` n `228`; crypto_major avg `0.7915` n `8`; equity avg `0.1449` n `65`; fx avg `-0.0055` n `5`; index avg `0.2051` n `23`; metal avg `0.229` n `18`; unknown avg `0.1482` n `375`
- 24h: commodity avg `-0.3652` n `12`; crypto_alt avg `4.3413` n `228`; crypto_major avg `2.7819` n `8`; equity avg `3.6656` n `65`; fx avg `0.0496` n `5`; index avg `1.4073` n `23`; metal avg `0.2321` n `18`; unknown avg `1.4955` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
