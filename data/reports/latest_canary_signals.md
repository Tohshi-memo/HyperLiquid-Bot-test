# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T12:37:21.147201+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0598` n `10`; crypto_alt avg `0.022` n `228`; crypto_major avg `-0.0405` n `7`; equity avg `0.0001` n `108`; fx avg `0.0088` n `6`; index avg `0.0044` n `24`; metal avg `0.0134` n `13`; unknown avg `0.0782` n `769`
- 1h: commodity avg `-0.0409` n `10`; crypto_alt avg `0.0313` n `228`; crypto_major avg `-0.1517` n `7`; equity avg `0.0051` n `108`; fx avg `0.0145` n `6`; index avg `-0.002` n `24`; metal avg `-0.0008` n `13`; unknown avg `0.083` n `769`
- 4h: commodity avg `-0.0917` n `10`; crypto_alt avg `0.0155` n `228`; crypto_major avg `-0.1004` n `7`; equity avg `-0.084` n `108`; fx avg `0.0113` n `6`; index avg `-0.0076` n `24`; metal avg `-0.0101` n `13`; unknown avg `0.0408` n `769`
- 24h: commodity avg `0.1582` n `10`; crypto_alt avg `1.05` n `228`; crypto_major avg `0.1526` n `7`; equity avg `0.4309` n `108`; fx avg `-0.0007` n `6`; index avg `0.0409` n `24`; metal avg `0.0712` n `13`; unknown avg `0.2941` n `736`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
