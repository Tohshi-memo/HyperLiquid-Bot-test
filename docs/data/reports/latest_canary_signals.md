# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T04:22:18.355062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0273` n `12`; crypto_alt avg `0.0884` n `228`; crypto_major avg `-0.0052` n `8`; equity avg `0.1508` n `67`; fx avg `0.0016` n `6`; index avg `0.0184` n `23`; metal avg `-0.0558` n `18`; unknown avg `0.2851` n `396`
- 1h: commodity avg `-0.2562` n `12`; crypto_alt avg `-0.0695` n `228`; crypto_major avg `-0.0796` n `8`; equity avg `0.0247` n `67`; fx avg `-0.0007` n `6`; index avg `-0.015` n `23`; metal avg `-0.0422` n `18`; unknown avg `-0.2642` n `396`
- 4h: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.165` n `228`; crypto_major avg `0.4308` n `8`; equity avg `0.2883` n `67`; fx avg `-0.022` n `6`; index avg `0.2309` n `23`; metal avg `0.2232` n `18`; unknown avg `-0.3661` n `396`
- 24h: commodity avg `-3.0577` n `12`; crypto_alt avg `1.8788` n `228`; crypto_major avg `2.2906` n `8`; equity avg `2.1856` n `67`; fx avg `0.0363` n `6`; index avg `1.1547` n `23`; metal avg `1.1642` n `18`; unknown avg `1.5533` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
