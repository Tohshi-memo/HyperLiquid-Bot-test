# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T00:22:14.188935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1287` n `12`; crypto_alt avg `-0.0893` n `228`; crypto_major avg `-0.2476` n `8`; equity avg `-0.1429` n `67`; fx avg `0.0` n `6`; index avg `-0.0885` n `23`; metal avg `-0.0131` n `18`; unknown avg `-0.0779` n `386`
- 1h: commodity avg `0.1425` n `12`; crypto_alt avg `-0.9496` n `228`; crypto_major avg `-0.6368` n `8`; equity avg `-0.3606` n `67`; fx avg `-0.0045` n `6`; index avg `-0.1005` n `23`; metal avg `-0.0959` n `18`; unknown avg `-0.5192` n `386`
- 4h: commodity avg `0.9494` n `12`; crypto_alt avg `-1.0706` n `228`; crypto_major avg `-0.6817` n `8`; equity avg `-0.6267` n `67`; fx avg `-0.0133` n `6`; index avg `-0.3008` n `23`; metal avg `-0.1359` n `18`; unknown avg `-0.701` n `386`
- 24h: commodity avg `-0.0816` n `12`; crypto_alt avg `-3.7125` n `228`; crypto_major avg `-2.7963` n `8`; equity avg `-1.8572` n `67`; fx avg `0.1458` n `6`; index avg `-0.038` n `23`; metal avg `-1.0006` n `18`; unknown avg `-1.9006` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
