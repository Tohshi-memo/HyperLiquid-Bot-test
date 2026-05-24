# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T03:22:15.168384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0992` n `12`; crypto_alt avg `-0.2553` n `228`; crypto_major avg `-0.0715` n `8`; equity avg `-0.0147` n `67`; fx avg `0.0024` n `6`; index avg `0.0025` n `23`; metal avg `0.08` n `18`; unknown avg `-0.0451` n `396`
- 1h: commodity avg `0.0745` n `12`; crypto_alt avg `-0.1796` n `228`; crypto_major avg `0.0098` n `8`; equity avg `-0.0037` n `67`; fx avg `-0.0079` n `6`; index avg `0.086` n `23`; metal avg `0.0609` n `18`; unknown avg `0.1399` n `396`
- 4h: commodity avg `0.1933` n `12`; crypto_alt avg `-0.1678` n `228`; crypto_major avg `0.548` n `8`; equity avg `0.2703` n `67`; fx avg `-0.0305` n `6`; index avg `0.353` n `23`; metal avg `0.3829` n `18`; unknown avg `0.2686` n `396`
- 24h: commodity avg `-2.6599` n `12`; crypto_alt avg `1.4465` n `228`; crypto_major avg `2.2694` n `8`; equity avg `2.1449` n `67`; fx avg `0.0357` n `6`; index avg `1.1733` n `23`; metal avg `1.1791` n `18`; unknown avg `1.6059` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
