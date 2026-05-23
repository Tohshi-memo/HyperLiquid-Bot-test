# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T06:07:15.027269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0128` n `12`; crypto_alt avg `-0.1224` n `228`; crypto_major avg `0.0092` n `8`; equity avg `0.0266` n `67`; fx avg `-0.0027` n `6`; index avg `0.0072` n `23`; metal avg `0.0085` n `18`; unknown avg `1.0098` n `376`
- 1h: commodity avg `-0.035` n `12`; crypto_alt avg `-0.195` n `228`; crypto_major avg `0.0066` n `8`; equity avg `0.0098` n `67`; fx avg `0.006` n `6`; index avg `-0.0133` n `23`; metal avg `-0.0005` n `18`; unknown avg `0.9403` n `376`
- 4h: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.3984` n `228`; crypto_major avg `0.0244` n `8`; equity avg `-0.0224` n `67`; fx avg `0.0052` n `6`; index avg `-0.0603` n `23`; metal avg `0.0021` n `18`; unknown avg `0.5577` n `376`
- 24h: commodity avg `-0.166` n `12`; crypto_alt avg `-3.9452` n `228`; crypto_major avg `-2.4657` n `8`; equity avg `-1.8914` n `67`; fx avg `0.0391` n `6`; index avg `-0.1569` n `23`; metal avg `-0.7682` n `18`; unknown avg `-1.2342` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
