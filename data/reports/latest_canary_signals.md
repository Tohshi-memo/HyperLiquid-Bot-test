# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T15:07:25.280243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `0.078` n `230`; crypto_major avg `0.1535` n `8`; equity avg `0.0024` n `100`; fx avg `0.0028` n `6`; index avg `0.0083` n `25`; metal avg `0.0013` n `20`; unknown avg `0.0543` n `774`
- 1h: commodity avg `0.0178` n `12`; crypto_alt avg `0.0977` n `230`; crypto_major avg `0.3234` n `8`; equity avg `0.0684` n `100`; fx avg `0.0012` n `6`; index avg `0.0045` n `25`; metal avg `0.0194` n `20`; unknown avg `-0.0378` n `774`
- 4h: commodity avg `-0.3745` n `12`; crypto_alt avg `0.2117` n `230`; crypto_major avg `0.3879` n `8`; equity avg `0.0226` n `100`; fx avg `-0.0054` n `6`; index avg `0.0016` n `25`; metal avg `0.0211` n `20`; unknown avg `-0.0568` n `774`
- 24h: commodity avg `-0.6148` n `12`; crypto_alt avg `0.1834` n `230`; crypto_major avg `0.5835` n `8`; equity avg `-0.6409` n `100`; fx avg `-0.0143` n `6`; index avg `-0.0391` n `25`; metal avg `-0.0469` n `20`; unknown avg `-0.4894` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1242`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1149`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1083`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
