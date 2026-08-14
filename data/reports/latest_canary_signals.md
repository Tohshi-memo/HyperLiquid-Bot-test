# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T00:22:28.178358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `12`; crypto_alt avg `0.0645` n `230`; crypto_major avg `0.0034` n `8`; equity avg `-0.1336` n `113`; fx avg `0.0039` n `6`; index avg `-0.0328` n `25`; metal avg `-0.0456` n `20`; unknown avg `0.5299` n `787`
- 1h: commodity avg `0.0142` n `12`; crypto_alt avg `0.1481` n `230`; crypto_major avg `0.0931` n `8`; equity avg `-0.125` n `113`; fx avg `-0.0035` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0657` n `20`; unknown avg `0.4824` n `787`
- 4h: commodity avg `0.0334` n `12`; crypto_alt avg `0.4032` n `230`; crypto_major avg `0.0278` n `8`; equity avg `0.1217` n `113`; fx avg `-0.0008` n `6`; index avg `0.0339` n `25`; metal avg `-0.0164` n `20`; unknown avg `0.5922` n `787`
- 24h: commodity avg `-0.383` n `12`; crypto_alt avg `0.2086` n `230`; crypto_major avg `0.4284` n `8`; equity avg `1.1652` n `113`; fx avg `0.0629` n `6`; index avg `0.2374` n `25`; metal avg `-0.677` n `20`; unknown avg `0.9697` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.243`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
