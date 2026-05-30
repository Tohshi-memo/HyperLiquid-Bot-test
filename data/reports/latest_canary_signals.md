# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T23:22:19.865504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0541` n `12`; crypto_alt avg `-0.1671` n `228`; crypto_major avg `-0.1018` n `8`; equity avg `0.0489` n `69`; fx avg `-0.0001` n `6`; index avg `0.0148` n `23`; metal avg `-0.005` n `18`; unknown avg `-0.0873` n `421`
- 1h: commodity avg `-0.0843` n `12`; crypto_alt avg `-0.2077` n `228`; crypto_major avg `0.035` n `8`; equity avg `0.1827` n `69`; fx avg `-0.0157` n `6`; index avg `0.005` n `23`; metal avg `-0.0307` n `18`; unknown avg `-0.3445` n `421`
- 4h: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.8433` n `228`; crypto_major avg `-0.454` n `8`; equity avg `0.2402` n `69`; fx avg `-0.0126` n `6`; index avg `-0.0214` n `23`; metal avg `-0.0266` n `18`; unknown avg `-0.6591` n `421`
- 24h: commodity avg `-0.2404` n `12`; crypto_alt avg `1.0521` n `228`; crypto_major avg `2.7091` n `8`; equity avg `1.1276` n `69`; fx avg `0.0275` n `6`; index avg `0.1114` n `23`; metal avg `0.0297` n `18`; unknown avg `1.2142` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
