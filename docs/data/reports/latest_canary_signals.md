# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T19:07:32.904278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1109` n `12`; crypto_alt avg `-0.0323` n `230`; crypto_major avg `0.0086` n `8`; equity avg `-0.26` n `100`; fx avg `0.0045` n `6`; index avg `-0.0277` n `25`; metal avg `-0.0089` n `20`; unknown avg `-0.032` n `772`
- 1h: commodity avg `-0.3712` n `12`; crypto_alt avg `0.1159` n `230`; crypto_major avg `0.1196` n `8`; equity avg `-0.211` n `100`; fx avg `0.0005` n `6`; index avg `-0.0272` n `25`; metal avg `0.0141` n `20`; unknown avg `-0.1138` n `772`
- 4h: commodity avg `-0.1134` n `12`; crypto_alt avg `-0.5663` n `230`; crypto_major avg `-0.4576` n `8`; equity avg `0.0001` n `100`; fx avg `0.0119` n `6`; index avg `-0.0093` n `25`; metal avg `-0.1091` n `20`; unknown avg `-0.5601` n `772`
- 24h: commodity avg `0.7098` n `12`; crypto_alt avg `-1.4598` n `230`; crypto_major avg `-2.044` n `8`; equity avg `-1.4796` n `99`; fx avg `-0.0788` n `6`; index avg `-0.3795` n `25`; metal avg `-0.8207` n `20`; unknown avg `-0.4425` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
