# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T23:52:14.023717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `-0.7215` n `228`; crypto_major avg `-0.2418` n `8`; equity avg `-0.0749` n `67`; fx avg `-0.0029` n `6`; index avg `0.0301` n `23`; metal avg `-0.0555` n `18`; unknown avg `-0.382` n `386`
- 1h: commodity avg `0.3542` n `12`; crypto_alt avg `-1.0188` n `228`; crypto_major avg `-0.3906` n `8`; equity avg `-0.1619` n `67`; fx avg `-0.0025` n `6`; index avg `-0.0859` n `23`; metal avg `-0.0727` n `18`; unknown avg `-0.5773` n `386`
- 4h: commodity avg `0.7772` n `12`; crypto_alt avg `-1.147` n `228`; crypto_major avg `-0.6041` n `8`; equity avg `-0.387` n `67`; fx avg `-0.0118` n `6`; index avg `-0.1375` n `23`; metal avg `-0.1367` n `18`; unknown avg `-0.8281` n `386`
- 24h: commodity avg `-0.1201` n `12`; crypto_alt avg `-4.0839` n `228`; crypto_major avg `-2.8505` n `8`; equity avg `-1.6416` n `67`; fx avg `0.1887` n `6`; index avg `0.1662` n `23`; metal avg `-1.0286` n `18`; unknown avg `-1.8568` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
