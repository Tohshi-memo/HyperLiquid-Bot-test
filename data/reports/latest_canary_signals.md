# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T06:22:25.053648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `12`; crypto_alt avg `0.0381` n `230`; crypto_major avg `0.0705` n `8`; equity avg `0.0237` n `96`; fx avg `0.0082` n `6`; index avg `0.0008` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0075` n `770`
- 1h: commodity avg `-0.0129` n `12`; crypto_alt avg `-0.062` n `230`; crypto_major avg `-0.0307` n `8`; equity avg `0.0048` n `96`; fx avg `0.0126` n `6`; index avg `-0.0002` n `25`; metal avg `0.0018` n `20`; unknown avg `0.0106` n `752`
- 4h: commodity avg `-0.0394` n `12`; crypto_alt avg `-0.0924` n `230`; crypto_major avg `-0.0704` n `8`; equity avg `0.0869` n `96`; fx avg `0.0054` n `6`; index avg `0.006` n `25`; metal avg `0.0013` n `20`; unknown avg `0.0045` n `752`
- 24h: commodity avg `0.3034` n `12`; crypto_alt avg `0.1438` n `230`; crypto_major avg `1.0066` n `8`; equity avg `0.0337` n `96`; fx avg `-0.0008` n `6`; index avg `-0.0521` n `25`; metal avg `-0.0044` n `20`; unknown avg `-0.0148` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
