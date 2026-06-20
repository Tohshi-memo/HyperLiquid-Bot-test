# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T20:52:25.705406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0095` n `12`; crypto_alt avg `0.1275` n `228`; crypto_major avg `0.1695` n `8`; equity avg `0.0406` n `78`; fx avg `0.0026` n `6`; index avg `-0.0002` n `23`; metal avg `0.0057` n `18`; unknown avg `0.099` n `701`
- 1h: commodity avg `-0.0317` n `12`; crypto_alt avg `-0.0753` n `228`; crypto_major avg `0.0662` n `8`; equity avg `0.0745` n `78`; fx avg `0.1834` n `6`; index avg `-0.014` n `23`; metal avg `0.015` n `18`; unknown avg `0.1418` n `701`
- 4h: commodity avg `-0.1015` n `12`; crypto_alt avg `-0.4079` n `228`; crypto_major avg `-0.0556` n `8`; equity avg `0.0783` n `78`; fx avg `-0.0083` n `6`; index avg `-0.0062` n `23`; metal avg `-0.0453` n `18`; unknown avg `0.1681` n `701`
- 24h: commodity avg `0.2253` n `12`; crypto_alt avg `0.5414` n `228`; crypto_major avg `1.038` n `8`; equity avg `0.5011` n `78`; fx avg `0.0586` n `6`; index avg `0.0604` n `23`; metal avg `-0.0604` n `18`; unknown avg `-0.1577` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
