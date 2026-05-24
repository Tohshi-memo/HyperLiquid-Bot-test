# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T03:52:16.513063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0237` n `12`; crypto_alt avg `-0.0985` n `228`; crypto_major avg `-0.0619` n `8`; equity avg `-0.0732` n `67`; fx avg `-0.0005` n `6`; index avg `-0.0332` n `23`; metal avg `-0.0057` n `18`; unknown avg `-0.2151` n `396`
- 1h: commodity avg `-0.2638` n `12`; crypto_alt avg `-0.4163` n `228`; crypto_major avg `-0.0753` n `8`; equity avg `-0.011` n `67`; fx avg `-0.0055` n `6`; index avg `-0.0884` n `23`; metal avg `0.1025` n `18`; unknown avg `-0.2801` n `396`
- 4h: commodity avg `0.2313` n `12`; crypto_alt avg `-0.4809` n `228`; crypto_major avg `0.368` n `8`; equity avg `0.1846` n `67`; fx avg `-0.0262` n `6`; index avg `0.2427` n `23`; metal avg `0.2932` n `18`; unknown avg `-0.2038` n `396`
- 24h: commodity avg `-2.9544` n `12`; crypto_alt avg `1.2046` n `228`; crypto_major avg `2.0001` n `8`; equity avg `2.125` n `67`; fx avg `0.0358` n `6`; index avg `1.1301` n `23`; metal avg `1.203` n `18`; unknown avg `1.7886` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
