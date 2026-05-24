# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T01:37:19.601590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0892` n `12`; crypto_alt avg `-0.0102` n `228`; crypto_major avg `0.0872` n `8`; equity avg `0.0292` n `67`; fx avg `-0.0093` n `6`; index avg `0.0236` n `23`; metal avg `-0.0029` n `18`; unknown avg `-0.3804` n `396`
- 1h: commodity avg `0.0738` n `12`; crypto_alt avg `0.1361` n `228`; crypto_major avg `0.4524` n `8`; equity avg `0.2198` n `67`; fx avg `0.0126` n `6`; index avg `0.1694` n `23`; metal avg `0.1491` n `18`; unknown avg `-0.2937` n `396`
- 4h: commodity avg `0.1925` n `12`; crypto_alt avg `-0.5002` n `228`; crypto_major avg `0.4369` n `8`; equity avg `0.3408` n `67`; fx avg `0.0378` n `6`; index avg `0.303` n `23`; metal avg `0.4348` n `18`; unknown avg `-0.251` n `396`
- 24h: commodity avg `-2.8884` n `12`; crypto_alt avg `2.3688` n `228`; crypto_major avg `2.6829` n `8`; equity avg `2.2594` n `67`; fx avg `0.0453` n `6`; index avg `1.1631` n `23`; metal avg `1.1738` n `18`; unknown avg `1.5785` n `376`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
