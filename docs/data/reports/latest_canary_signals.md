# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T12:05:16.285519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `-0.1542` n `230`; crypto_major avg `-0.1798` n `8`; equity avg `-0.0516` n `96`; fx avg `0.0046` n `6`; index avg `-0.0125` n `25`; metal avg `-0.005` n `20`; unknown avg `-0.053` n `770`
- 1h: commodity avg `-0.0194` n `12`; crypto_alt avg `-0.454` n `230`; crypto_major avg `-0.3128` n `8`; equity avg `-0.0974` n `96`; fx avg `-0.0085` n `6`; index avg `-0.011` n `25`; metal avg `-0.0137` n `20`; unknown avg `-0.0568` n `770`
- 4h: commodity avg `0.0003` n `12`; crypto_alt avg `-0.3986` n `230`; crypto_major avg `-0.2488` n `8`; equity avg `-0.1681` n `96`; fx avg `-0.0202` n `6`; index avg `0.0029` n `25`; metal avg `-0.0412` n `20`; unknown avg `-0.0694` n `770`
- 24h: commodity avg `0.1795` n `12`; crypto_alt avg `-0.0954` n `230`; crypto_major avg `0.7022` n `8`; equity avg `0.0876` n `96`; fx avg `-0.0082` n `6`; index avg `-0.0466` n `25`; metal avg `-0.0863` n `20`; unknown avg `0.0808` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1151`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1139`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
