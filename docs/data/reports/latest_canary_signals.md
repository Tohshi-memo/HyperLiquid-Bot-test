# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T08:37:25.592543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1844` n `12`; crypto_alt avg `0.0446` n `228`; crypto_major avg `0.0541` n `8`; equity avg `-0.0009` n `74`; fx avg `0.016` n `6`; index avg `0.0438` n `23`; metal avg `-0.0827` n `18`; unknown avg `0.0085` n `547`
- 1h: commodity avg `-0.1206` n `12`; crypto_alt avg `0.0471` n `228`; crypto_major avg `-0.0175` n `8`; equity avg `0.0372` n `74`; fx avg `0.0786` n `6`; index avg `0.2036` n `23`; metal avg `0.2859` n `18`; unknown avg `-0.02` n `547`
- 4h: commodity avg `-0.0968` n `12`; crypto_alt avg `0.2042` n `228`; crypto_major avg `-0.255` n `8`; equity avg `0.0235` n `74`; fx avg `0.0945` n `6`; index avg `0.1745` n `23`; metal avg `0.5914` n `18`; unknown avg `0.1675` n `503`
- 24h: commodity avg `-1.1488` n `12`; crypto_alt avg `0.3391` n `228`; crypto_major avg `0.8548` n `8`; equity avg `2.1329` n `74`; fx avg `0.0294` n `6`; index avg `1.136` n `23`; metal avg `1.0887` n `18`; unknown avg `-2.6318` n `503`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
