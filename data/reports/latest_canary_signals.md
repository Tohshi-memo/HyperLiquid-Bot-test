# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T06:37:18.752992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0877` n `12`; crypto_alt avg `-0.3362` n `228`; crypto_major avg `-0.2758` n `8`; equity avg `0.0307` n `69`; fx avg `0.0134` n `6`; index avg `-0.0709` n `23`; metal avg `-0.1156` n `18`; unknown avg `-0.1808` n `417`
- 1h: commodity avg `-0.0765` n `12`; crypto_alt avg `0.1924` n `228`; crypto_major avg `0.2537` n `8`; equity avg `0.2444` n `69`; fx avg `0.0476` n `6`; index avg `0.0032` n `23`; metal avg `0.0157` n `18`; unknown avg `0.0297` n `407`
- 4h: commodity avg `-0.1035` n `12`; crypto_alt avg `0.0823` n `228`; crypto_major avg `0.3895` n `8`; equity avg `0.6293` n `69`; fx avg `0.0696` n `6`; index avg `0.1871` n `23`; metal avg `0.0021` n `18`; unknown avg `-0.107` n `407`
- 24h: commodity avg `0.0068` n `12`; crypto_alt avg `1.8845` n `228`; crypto_major avg `2.3917` n `8`; equity avg `4.0788` n `69`; fx avg `0.1985` n `6`; index avg `1.4269` n `23`; metal avg `1.9601` n `18`; unknown avg `0.8678` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
