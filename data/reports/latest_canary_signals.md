# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T21:52:20.341489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0588` n `12`; crypto_alt avg `0.0237` n `228`; crypto_major avg `0.0816` n `8`; equity avg `-0.0084` n `67`; fx avg `0.001` n `6`; index avg `-0.053` n `23`; metal avg `0.037` n `18`; unknown avg `0.0067` n `386`
- 1h: commodity avg `0.1842` n `12`; crypto_alt avg `0.2841` n `228`; crypto_major avg `0.3412` n `8`; equity avg `-0.0168` n `67`; fx avg `0.0058` n `6`; index avg `-0.0621` n `23`; metal avg `0.0749` n `18`; unknown avg `-0.0414` n `386`
- 4h: commodity avg `0.591` n `12`; crypto_alt avg `-2.188` n `228`; crypto_major avg `-1.3114` n `8`; equity avg `-0.9316` n `67`; fx avg `0.0278` n `6`; index avg `-0.3797` n `23`; metal avg `-0.2944` n `18`; unknown avg `0.93` n `386`
- 24h: commodity avg `-0.854` n `12`; crypto_alt avg `-2.66` n `228`; crypto_major avg `-1.8395` n `8`; equity avg `-1.1196` n `67`; fx avg `0.1852` n `6`; index avg `0.446` n `23`; metal avg `-0.9744` n `18`; unknown avg `-1.1557` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
