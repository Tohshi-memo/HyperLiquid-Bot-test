# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T02:03:39.135107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `-0.0654` n `230`; crypto_major avg `0.022` n `8`; equity avg `0.007` n `100`; fx avg `0.0006` n `6`; index avg `-0.0078` n `25`; metal avg `0.001` n `20`; unknown avg `0.0217` n `774`
- 1h: commodity avg `0.0364` n `12`; crypto_alt avg `-0.2642` n `230`; crypto_major avg `-0.0303` n `8`; equity avg `-0.0424` n `100`; fx avg `-0.011` n `6`; index avg `-0.0203` n `25`; metal avg `-0.0072` n `20`; unknown avg `0.1659` n `774`
- 4h: commodity avg `-0.0588` n `12`; crypto_alt avg `0.1957` n `230`; crypto_major avg `0.3016` n `8`; equity avg `-0.0497` n `100`; fx avg `0.034` n `6`; index avg `0.0141` n `25`; metal avg `-0.0059` n `20`; unknown avg `-0.1491` n `774`
- 24h: commodity avg `-0.2838` n `12`; crypto_alt avg `-1.0545` n `230`; crypto_major avg `-0.826` n `8`; equity avg `-2.8884` n `100`; fx avg `-0.0271` n `6`; index avg `-0.2855` n `25`; metal avg `0.0957` n `20`; unknown avg `14.0147` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1224`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1159`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1072`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1066`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `666`, weak_sample_signal
