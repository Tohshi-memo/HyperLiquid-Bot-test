# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T05:22:17.298638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `-0.1952` n `228`; crypto_major avg `-0.0932` n `8`; equity avg `-0.0286` n `67`; fx avg `-0.0194` n `6`; index avg `-0.0035` n `23`; metal avg `-0.0078` n `18`; unknown avg `0.0848` n `396`
- 1h: commodity avg `0.0016` n `12`; crypto_alt avg `-0.4218` n `228`; crypto_major avg `-0.0685` n `8`; equity avg `0.0594` n `67`; fx avg `0.0147` n `6`; index avg `-0.019` n `23`; metal avg `0.0117` n `18`; unknown avg `-0.3044` n `396`
- 4h: commodity avg `-0.1174` n `12`; crypto_alt avg `-0.9337` n `228`; crypto_major avg `-0.3033` n `8`; equity avg `0.0969` n `67`; fx avg `-0.0069` n `6`; index avg `0.0665` n `23`; metal avg `0.0502` n `18`; unknown avg `-0.8386` n `396`
- 24h: commodity avg `-3.0751` n `12`; crypto_alt avg `1.8196` n `228`; crypto_major avg `2.5048` n `8`; equity avg `2.3733` n `67`; fx avg `0.0448` n `6`; index avg `1.2213` n `23`; metal avg `1.2119` n `18`; unknown avg `1.7408` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
