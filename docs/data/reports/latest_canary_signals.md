# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T06:03:19.253520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0675` n `12`; crypto_alt avg `0.0056` n `230`; crypto_major avg `-0.072` n `8`; equity avg `-0.0651` n `113`; fx avg `-0.0139` n `6`; index avg `0.0016` n `25`; metal avg `0.0615` n `20`; unknown avg `0.0039` n `755`
- 1h: commodity avg `0.1587` n `12`; crypto_alt avg `-0.0059` n `230`; crypto_major avg `-0.0763` n `8`; equity avg `0.018` n `113`; fx avg `-0.034` n `6`; index avg `0.054` n `25`; metal avg `0.1685` n `20`; unknown avg `0.1123` n `755`
- 4h: commodity avg `0.2278` n `12`; crypto_alt avg `-0.4771` n `230`; crypto_major avg `-0.4681` n `8`; equity avg `-0.0837` n `113`; fx avg `-0.0244` n `6`; index avg `0.012` n `25`; metal avg `0.1798` n `20`; unknown avg `-0.0785` n `755`
- 24h: commodity avg `-0.274` n `12`; crypto_alt avg `-0.4002` n `230`; crypto_major avg `-0.6557` n `8`; equity avg `0.8202` n `113`; fx avg `-0.0227` n `6`; index avg `0.2717` n `25`; metal avg `-0.2929` n `20`; unknown avg `0.9278` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2385`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2004`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1887`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
