# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T01:52:23.508484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `12`; crypto_alt avg `0.0899` n `230`; crypto_major avg `0.0125` n `8`; equity avg `0.0545` n `113`; fx avg `-0.0185` n `6`; index avg `0.0198` n `25`; metal avg `-0.0356` n `20`; unknown avg `0.0135` n `787`
- 1h: commodity avg `-0.0229` n `12`; crypto_alt avg `0.0511` n `230`; crypto_major avg `-0.0432` n `8`; equity avg `-0.1849` n `113`; fx avg `-0.0327` n `6`; index avg `-0.0391` n `25`; metal avg `-0.0977` n `20`; unknown avg `-0.0395` n `787`
- 4h: commodity avg `-0.0339` n `12`; crypto_alt avg `0.1432` n `230`; crypto_major avg `0.0836` n `8`; equity avg `-0.31` n `113`; fx avg `-0.0585` n `6`; index avg `-0.0471` n `25`; metal avg `-0.2248` n `20`; unknown avg `0.7126` n `787`
- 24h: commodity avg `-0.353` n `12`; crypto_alt avg `0.4079` n `230`; crypto_major avg `0.5181` n `8`; equity avg `0.9445` n `113`; fx avg `0.0113` n `6`; index avg `0.226` n `25`; metal avg `-0.6586` n `20`; unknown avg `1.1769` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2436`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
