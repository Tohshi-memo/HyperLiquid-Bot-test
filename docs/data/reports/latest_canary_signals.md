# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T23:37:29.352539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `0.0522` n `230`; crypto_major avg `0.0255` n `8`; equity avg `-0.015` n `113`; fx avg `-0.0018` n `6`; index avg `0.0108` n `25`; metal avg `0.0118` n `20`; unknown avg `0.053` n `787`
- 1h: commodity avg `0.0318` n `12`; crypto_alt avg `-0.0111` n `230`; crypto_major avg `-0.1666` n `8`; equity avg `-0.0237` n `113`; fx avg `0.0018` n `6`; index avg `0.0114` n `25`; metal avg `0.0292` n `20`; unknown avg `0.2722` n `787`
- 4h: commodity avg `0.0107` n `12`; crypto_alt avg `0.3295` n `230`; crypto_major avg `-0.0166` n `8`; equity avg `0.2008` n `113`; fx avg `0.0008` n `6`; index avg `0.0464` n `25`; metal avg `0.0627` n `20`; unknown avg `0.1822` n `787`
- 24h: commodity avg `-0.448` n `12`; crypto_alt avg `0.6321` n `230`; crypto_major avg `0.6279` n `8`; equity avg `1.593` n `113`; fx avg `0.0217` n `6`; index avg `0.3478` n `25`; metal avg `-0.4304` n `20`; unknown avg `0.2268` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2439`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1998`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
