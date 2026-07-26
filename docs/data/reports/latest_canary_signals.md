# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T02:22:27.625053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `0.1146` n `230`; crypto_major avg `0.166` n `8`; equity avg `0.0469` n `100`; fx avg `-0.0047` n `6`; index avg `0.0008` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.0559` n `774`
- 1h: commodity avg `0.0517` n `12`; crypto_alt avg `0.1528` n `230`; crypto_major avg `0.2226` n `8`; equity avg `0.0808` n `100`; fx avg `0.0039` n `6`; index avg `0.0214` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.1016` n `774`
- 4h: commodity avg `-0.0149` n `12`; crypto_alt avg `0.0753` n `230`; crypto_major avg `0.2754` n `8`; equity avg `0.1871` n `100`; fx avg `-0.0003` n `6`; index avg `0.0403` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.2751` n `774`
- 24h: commodity avg `-0.4915` n `12`; crypto_alt avg `0.7311` n `230`; crypto_major avg `1.299` n `8`; equity avg `0.6104` n `100`; fx avg `-0.0079` n `6`; index avg `0.1677` n `25`; metal avg `0.0326` n `20`; unknown avg `-0.2251` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1362`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1234`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.118`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1168`, n `666`, weak_sample_signal
