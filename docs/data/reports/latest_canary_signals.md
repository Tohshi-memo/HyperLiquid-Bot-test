# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T05:52:19.733357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.59` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.8682` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5778` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0692` n `12`; crypto_alt avg `-0.1965` n `228`; crypto_major avg `-0.1525` n `8`; equity avg `-0.0706` n `69`; fx avg `0.0066` n `6`; index avg `0.0759` n `23`; metal avg `-0.1468` n `18`; unknown avg `0.8422` n `422`
- 1h: commodity avg `-0.0756` n `12`; crypto_alt avg `-0.6667` n `228`; crypto_major avg `-0.7259` n `8`; equity avg `0.1912` n `69`; fx avg `0.0047` n `6`; index avg `0.2516` n `23`; metal avg `0.4652` n `18`; unknown avg `1.0499` n `422`
- 4h: commodity avg `-0.3442` n `12`; crypto_alt avg `-0.0944` n `228`; crypto_major avg `-0.443` n `8`; equity avg `1.1348` n `69`; fx avg `0.0052` n `6`; index avg `0.4844` n `23`; metal avg `1.4252` n `18`; unknown avg `0.2036` n `422`
- 24h: commodity avg `-0.8149` n `12`; crypto_alt avg `-1.1514` n `228`; crypto_major avg `-1.8206` n `8`; equity avg `-0.1378` n `69`; fx avg `0.1248` n `6`; index avg `-0.23` n `23`; metal avg `0.5409` n `18`; unknown avg `2.9818` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
