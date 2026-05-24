# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T04:52:19.556284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `0.0201` n `228`; crypto_major avg `0.0529` n `8`; equity avg `0.0498` n `67`; fx avg `0.0222` n `6`; index avg `-0.0072` n `23`; metal avg `0.0137` n `18`; unknown avg `-0.2485` n `396`
- 1h: commodity avg `-0.0711` n `12`; crypto_alt avg `0.1731` n `228`; crypto_major avg `0.0163` n `8`; equity avg `0.1392` n `67`; fx avg `0.033` n `6`; index avg `-0.005` n `23`; metal avg `-0.027` n `18`; unknown avg `-0.4506` n `396`
- 4h: commodity avg `-0.1414` n `12`; crypto_alt avg `-0.3393` n `228`; crypto_major avg `0.1111` n `8`; equity avg `0.2203` n `67`; fx avg `0.0183` n `6`; index avg `0.167` n `23`; metal avg `0.183` n `18`; unknown avg `-0.6388` n `396`
- 24h: commodity avg `-2.9018` n `12`; crypto_alt avg `1.9156` n `228`; crypto_major avg `2.4788` n `8`; equity avg `2.3314` n `67`; fx avg `0.07` n `6`; index avg `1.16` n `23`; metal avg `1.2055` n `18`; unknown avg `1.8271` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
