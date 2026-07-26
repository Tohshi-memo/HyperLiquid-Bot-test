# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T00:22:28.522592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `12`; crypto_alt avg `0.0186` n `230`; crypto_major avg `0.0669` n `8`; equity avg `0.0142` n `100`; fx avg `-0.0052` n `6`; index avg `0.0009` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.0958` n `774`
- 1h: commodity avg `0.0167` n `12`; crypto_alt avg `0.0447` n `230`; crypto_major avg `0.146` n `8`; equity avg `0.0789` n `100`; fx avg `-0.0117` n `6`; index avg `0.0186` n `25`; metal avg `0.01` n `20`; unknown avg `-0.1886` n `774`
- 4h: commodity avg `-0.0281` n `12`; crypto_alt avg `-0.0191` n `230`; crypto_major avg `0.0703` n `8`; equity avg `0.1415` n `100`; fx avg `-0.0113` n `6`; index avg `0.0311` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.2905` n `774`
- 24h: commodity avg `-0.5434` n `12`; crypto_alt avg `0.377` n `230`; crypto_major avg `1.0699` n `8`; equity avg `0.506` n `100`; fx avg `-0.0206` n `6`; index avg `0.1421` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.2507` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.135`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1234`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.122`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1165`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1152`, n `666`, weak_sample_signal
