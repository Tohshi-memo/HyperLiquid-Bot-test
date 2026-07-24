# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T08:37:24.771236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1107` n `12`; crypto_alt avg `0.0643` n `230`; crypto_major avg `0.0884` n `8`; equity avg `0.139` n `100`; fx avg `-0.012` n `6`; index avg `0.0426` n `25`; metal avg `0.054` n `20`; unknown avg `0.014` n `772`
- 1h: commodity avg `-0.1125` n `12`; crypto_alt avg `-0.0419` n `230`; crypto_major avg `0.0302` n `8`; equity avg `0.004` n `100`; fx avg `-0.0436` n `6`; index avg `0.0141` n `25`; metal avg `0.0044` n `20`; unknown avg `0.03` n `772`
- 4h: commodity avg `-0.4163` n `12`; crypto_alt avg `0.3413` n `230`; crypto_major avg `0.4994` n `8`; equity avg `0.5421` n `100`; fx avg `-0.0209` n `6`; index avg `0.1183` n `25`; metal avg `0.2456` n `20`; unknown avg `0.1266` n `756`
- 24h: commodity avg `-0.1336` n `12`; crypto_alt avg `-0.891` n `230`; crypto_major avg `-1.2005` n `8`; equity avg `-1.694` n `99`; fx avg `-0.1535` n `6`; index avg `-0.4348` n `25`; metal avg `-0.4404` n `20`; unknown avg `0.1236` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.098`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0852`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0818`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0815`, n `666`, weak_sample_signal
