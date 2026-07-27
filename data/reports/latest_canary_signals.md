# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T06:37:28.340877+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0672` n `12`; crypto_alt avg `0.0536` n `230`; crypto_major avg `0.1723` n `8`; equity avg `0.046` n `100`; fx avg `0.0293` n `6`; index avg `-0.003` n `25`; metal avg `0.034` n `20`; unknown avg `0.1541` n `775`
- 1h: commodity avg `-0.3061` n `12`; crypto_alt avg `0.1558` n `230`; crypto_major avg `0.3701` n `8`; equity avg `0.2789` n `100`; fx avg `0.0425` n `6`; index avg `0.019` n `25`; metal avg `0.1127` n `20`; unknown avg `0.0014` n `759`
- 4h: commodity avg `-0.4209` n `12`; crypto_alt avg `0.127` n `230`; crypto_major avg `0.5984` n `8`; equity avg `0.6489` n `100`; fx avg `0.0346` n `6`; index avg `0.1197` n `25`; metal avg `0.0532` n `20`; unknown avg `0.003` n `759`
- 24h: commodity avg `-0.8302` n `12`; crypto_alt avg `1.2646` n `230`; crypto_major avg `1.8293` n `8`; equity avg `1.3394` n `100`; fx avg `0.1168` n `6`; index avg `0.1895` n `25`; metal avg `0.4431` n `20`; unknown avg `-0.0298` n `759`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
