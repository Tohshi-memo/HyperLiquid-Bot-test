# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T06:37:20.815543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0712` n `12`; crypto_alt avg `0.0104` n `228`; crypto_major avg `-0.0582` n `8`; equity avg `-0.001` n `69`; fx avg `0.0121` n `6`; index avg `0.0036` n `23`; metal avg `0.0092` n `18`; unknown avg `1.1868` n `421`
- 1h: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.2787` n `228`; crypto_major avg `-0.2215` n `8`; equity avg `0.0812` n `69`; fx avg `0.0115` n `6`; index avg `-0.0692` n `23`; metal avg `-0.0217` n `18`; unknown avg `-0.1031` n `401`
- 4h: commodity avg `0.0841` n `12`; crypto_alt avg `0.2848` n `228`; crypto_major avg `0.2445` n `8`; equity avg `0.2211` n `69`; fx avg `0.0261` n `6`; index avg `0.0108` n `23`; metal avg `0.0091` n `18`; unknown avg `0.0718` n `401`
- 24h: commodity avg `0.0713` n `12`; crypto_alt avg `0.2799` n `228`; crypto_major avg `2.0968` n `8`; equity avg `0.9785` n `69`; fx avg `0.0527` n `6`; index avg `-0.023` n `23`; metal avg `-0.0347` n `18`; unknown avg `1.3229` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
