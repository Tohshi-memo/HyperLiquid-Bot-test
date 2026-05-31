# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T07:37:16.080787+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `-0.3117` n `228`; crypto_major avg `-0.1927` n `8`; equity avg `0.1706` n `69`; fx avg `-0.0037` n `6`; index avg `0.0581` n `23`; metal avg `-0.0033` n `18`; unknown avg `-0.0557` n `421`
- 1h: commodity avg `0.1113` n `12`; crypto_alt avg `-0.637` n `228`; crypto_major avg `-0.5394` n `8`; equity avg `0.2245` n `69`; fx avg `0.0044` n `6`; index avg `-0.014` n `23`; metal avg `-0.0002` n `18`; unknown avg `-0.1549` n `421`
- 4h: commodity avg `0.2292` n `12`; crypto_alt avg `-0.6541` n `228`; crypto_major avg `-0.6332` n `8`; equity avg `0.3706` n `69`; fx avg `0.0165` n `6`; index avg `-0.0527` n `23`; metal avg `0.0089` n `18`; unknown avg `-0.1074` n `401`
- 24h: commodity avg `0.181` n `12`; crypto_alt avg `0.0619` n `228`; crypto_major avg `1.5978` n `8`; equity avg `1.2032` n `69`; fx avg `0.0566` n `6`; index avg `-0.0719` n `23`; metal avg `-0.0413` n `18`; unknown avg `0.6647` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
