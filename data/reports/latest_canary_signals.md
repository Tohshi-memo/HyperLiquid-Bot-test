# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T11:22:20.066773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1254` n `12`; crypto_alt avg `0.1678` n `228`; crypto_major avg `0.0847` n `8`; equity avg `-0.0107` n `69`; fx avg `-0.0105` n `6`; index avg `0.0899` n `23`; metal avg `0.0493` n `18`; unknown avg `0.8978` n `417`
- 1h: commodity avg `-0.1778` n `12`; crypto_alt avg `0.0532` n `228`; crypto_major avg `-0.0307` n `8`; equity avg `-0.0352` n `69`; fx avg `-0.0054` n `6`; index avg `0.2245` n `23`; metal avg `0.2009` n `18`; unknown avg `0.8972` n `417`
- 4h: commodity avg `-0.2668` n `12`; crypto_alt avg `-0.3067` n `228`; crypto_major avg `-0.0694` n `8`; equity avg `-0.262` n `69`; fx avg `-0.0468` n `6`; index avg `0.2183` n `23`; metal avg `0.2397` n `18`; unknown avg `0.7612` n `417`
- 24h: commodity avg `-0.1561` n `12`; crypto_alt avg `2.0709` n `228`; crypto_major avg `2.3226` n `8`; equity avg `3.6079` n `69`; fx avg `0.1577` n `6`; index avg `1.6302` n `23`; metal avg `2.2449` n `18`; unknown avg `1.8568` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
