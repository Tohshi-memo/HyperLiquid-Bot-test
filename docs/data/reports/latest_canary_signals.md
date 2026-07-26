# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T15:37:26.504923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `0.0947` n `230`; crypto_major avg `0.0986` n `8`; equity avg `0.0089` n `100`; fx avg `-0.0041` n `6`; index avg `-0.0118` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0234` n `775`
- 1h: commodity avg `-0.0337` n `12`; crypto_alt avg `0.305` n `230`; crypto_major avg `0.4902` n `8`; equity avg `0.092` n `100`; fx avg `-0.0054` n `6`; index avg `0.0078` n `25`; metal avg `-0.0058` n `20`; unknown avg `0.0056` n `775`
- 4h: commodity avg `0.0561` n `12`; crypto_alt avg `0.0861` n `230`; crypto_major avg `0.4055` n `8`; equity avg `0.131` n `100`; fx avg `-0.002` n `6`; index avg `0.0117` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.0689` n `775`
- 24h: commodity avg `-0.4322` n `12`; crypto_alt avg `1.2153` n `230`; crypto_major avg `1.4791` n `8`; equity avg `0.893` n `100`; fx avg `0.0125` n `6`; index avg `0.1738` n `25`; metal avg `0.1689` n `20`; unknown avg `0.1579` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
