# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T06:22:28.134022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0173` n `12`; crypto_alt avg `-0.0409` n `230`; crypto_major avg `0.0167` n `8`; equity avg `0.0109` n `100`; fx avg `0.002` n `6`; index avg `0.0032` n `25`; metal avg `-0.0008` n `20`; unknown avg `0.0068` n `774`
- 1h: commodity avg `0.0324` n `12`; crypto_alt avg `-0.2077` n `230`; crypto_major avg `-0.2055` n `8`; equity avg `0.0159` n `100`; fx avg `0.0008` n `6`; index avg `0.003` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.0237` n `758`
- 4h: commodity avg `-0.0484` n `12`; crypto_alt avg `-0.1171` n `230`; crypto_major avg `-0.1436` n `8`; equity avg `0.2043` n `100`; fx avg `-0.0077` n `6`; index avg `0.0523` n `25`; metal avg `-0.0121` n `20`; unknown avg `-0.0939` n `758`
- 24h: commodity avg `-0.294` n `12`; crypto_alt avg `-1.6467` n `230`; crypto_major avg `-1.3888` n `8`; equity avg `-2.3902` n `100`; fx avg `-0.0817` n `6`; index avg `-0.1429` n `25`; metal avg `0.1176` n `20`; unknown avg `13.7032` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1144`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1029`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
