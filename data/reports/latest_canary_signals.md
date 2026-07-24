# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T09:37:48.467417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `0.1054` n `230`; crypto_major avg `0.0642` n `8`; equity avg `0.1144` n `100`; fx avg `0.0105` n `6`; index avg `0.0208` n `25`; metal avg `-0.0035` n `20`; unknown avg `0.1559` n `773`
- 1h: commodity avg `-0.1499` n `12`; crypto_alt avg `-0.2385` n `230`; crypto_major avg `-0.3809` n `8`; equity avg `0.0988` n `100`; fx avg `-0.0112` n `6`; index avg `0.0247` n `25`; metal avg `0.0464` n `20`; unknown avg `0.1207` n `772`
- 4h: commodity avg `-0.5227` n `12`; crypto_alt avg `0.099` n `230`; crypto_major avg `0.0993` n `8`; equity avg `0.3862` n `100`; fx avg `-0.0212` n `6`; index avg `0.1014` n `25`; metal avg `0.2709` n `20`; unknown avg `0.1761` n `756`
- 24h: commodity avg `-0.3343` n `12`; crypto_alt avg `-1.1973` n `230`; crypto_major avg `-1.6655` n `8`; equity avg `-1.7651` n `99`; fx avg `-0.1442` n `6`; index avg `-0.4331` n `25`; metal avg `-0.3735` n `20`; unknown avg `0.1927` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0983`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.089`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0813`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0806`, n `666`, weak_sample_signal
