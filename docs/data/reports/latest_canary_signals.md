# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T06:37:24.785640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `0.0585` n `230`; crypto_major avg `0.095` n `8`; equity avg `0.0527` n `114`; fx avg `0.0023` n `6`; index avg `0.0021` n `25`; metal avg `-0.037` n `20`; unknown avg `0.0684` n `793`
- 1h: commodity avg `0.1238` n `12`; crypto_alt avg `0.6531` n `230`; crypto_major avg `0.5873` n `8`; equity avg `0.1373` n `114`; fx avg `0.0164` n `6`; index avg `-0.0117` n `25`; metal avg `0.1001` n `20`; unknown avg `0.0687` n `761`
- 4h: commodity avg `0.1064` n `12`; crypto_alt avg `0.1236` n `230`; crypto_major avg `0.4885` n `8`; equity avg `-0.1682` n `114`; fx avg `0.0179` n `6`; index avg `-0.1215` n `25`; metal avg `0.034` n `20`; unknown avg `0.043` n `761`
- 24h: commodity avg `0.83` n `12`; crypto_alt avg `-0.983` n `230`; crypto_major avg `0.3124` n `8`; equity avg `-1.5229` n `114`; fx avg `0.0048` n `6`; index avg `-0.4379` n `25`; metal avg `-0.1554` n `20`; unknown avg `0.0356` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1726`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
