# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T07:52:20.735572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0391` n `12`; crypto_alt avg `0.0048` n `228`; crypto_major avg `0.0191` n `8`; equity avg `0.0392` n `69`; fx avg `-0.0146` n `6`; index avg `0.0029` n `23`; metal avg `0.0076` n `18`; unknown avg `0.7272` n `421`
- 1h: commodity avg `0.1739` n `12`; crypto_alt avg `-0.6983` n `228`; crypto_major avg `-0.4229` n `8`; equity avg `0.2329` n `69`; fx avg `-0.0204` n `6`; index avg `-0.0174` n `23`; metal avg `-0.0107` n `18`; unknown avg `0.7932` n `421`
- 4h: commodity avg `0.2916` n `12`; crypto_alt avg `-0.6944` n `228`; crypto_major avg `-0.6265` n `8`; equity avg `0.4203` n `69`; fx avg `-0.0018` n `6`; index avg `-0.0228` n `23`; metal avg `0.016` n `18`; unknown avg `0.0104` n `401`
- 24h: commodity avg `0.2243` n `12`; crypto_alt avg `0.0064` n `228`; crypto_major avg `1.555` n `8`; equity avg `1.219` n `69`; fx avg `0.0419` n `6`; index avg `-0.0658` n `23`; metal avg `-0.0225` n `18`; unknown avg `1.5122` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
