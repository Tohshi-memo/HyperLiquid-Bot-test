# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T00:52:27.953573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.0513` n `231`; crypto_major avg `-0.0319` n `8`; equity avg `-0.0217` n `128`; fx avg `0.0012` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.034` n `793`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `-0.1085` n `231`; crypto_major avg `-0.0512` n `8`; equity avg `-0.0154` n `128`; fx avg `0.008` n `6`; index avg `0.0188` n `26`; metal avg `-0.0088` n `20`; unknown avg `4.029` n `793`
- 4h: commodity avg `-0.002` n `12`; crypto_alt avg `0.0438` n `231`; crypto_major avg `0.1374` n `8`; equity avg `0.0112` n `128`; fx avg `0.018` n `6`; index avg `0.0191` n `26`; metal avg `-0.002` n `20`; unknown avg `3.8028` n `774`
- 24h: commodity avg `-0.0218` n `12`; crypto_alt avg `0.229` n `231`; crypto_major avg `1.0005` n `8`; equity avg `0.3864` n `128`; fx avg `-0.0048` n `6`; index avg `0.1123` n `26`; metal avg `0.0936` n `20`; unknown avg `0.1507` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2252`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
