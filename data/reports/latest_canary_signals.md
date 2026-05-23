# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T00:37:21.019396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `-0.1809` n `228`; crypto_major avg `-0.1106` n `8`; equity avg `-0.1517` n `67`; fx avg `0.0` n `6`; index avg `-0.0573` n `23`; metal avg `-0.0332` n `18`; unknown avg `-0.2251` n `386`
- 1h: commodity avg `0.048` n `12`; crypto_alt avg `-0.9657` n `228`; crypto_major avg `-0.7374` n `8`; equity avg `-0.4745` n `67`; fx avg `-0.0045` n `6`; index avg `-0.1339` n `23`; metal avg `-0.113` n `18`; unknown avg `-0.6958` n `386`
- 4h: commodity avg `0.8357` n `12`; crypto_alt avg `-1.21` n `228`; crypto_major avg `-0.8438` n `8`; equity avg `-0.784` n `67`; fx avg `-0.0024` n `6`; index avg `-0.2881` n `23`; metal avg `-0.1362` n `18`; unknown avg `-0.8341` n `386`
- 24h: commodity avg `-0.1897` n `12`; crypto_alt avg `-3.9049` n `228`; crypto_major avg `-2.9366` n `8`; equity avg `-2.0494` n `67`; fx avg `0.1425` n `6`; index avg `-0.1125` n `23`; metal avg `-1.1335` n `18`; unknown avg `-2.0151` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
