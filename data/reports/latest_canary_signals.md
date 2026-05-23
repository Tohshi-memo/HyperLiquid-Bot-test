# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T05:07:18.958033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.171` n `12`; crypto_alt avg `-0.0758` n `228`; crypto_major avg `0.014` n `8`; equity avg `-0.0264` n `67`; fx avg `0.0011` n `6`; index avg `-0.0508` n `23`; metal avg `-0.0005` n `18`; unknown avg `0.1995` n `386`
- 1h: commodity avg `0.0148` n `12`; crypto_alt avg `-0.3902` n `228`; crypto_major avg `-0.3426` n `8`; equity avg `-0.1091` n `67`; fx avg `0.0011` n `6`; index avg `-0.0863` n `23`; metal avg `-0.0254` n `18`; unknown avg `0.4682` n `386`
- 4h: commodity avg `0.0549` n `12`; crypto_alt avg `0.1488` n `228`; crypto_major avg `-0.0374` n `8`; equity avg `0.0163` n `67`; fx avg `-0.0014` n `6`; index avg `-0.0043` n `23`; metal avg `0.0227` n `18`; unknown avg `-1.0457` n `386`
- 24h: commodity avg `0.1723` n `12`; crypto_alt avg `-3.9749` n `228`; crypto_major avg `-2.7902` n `8`; equity avg `-2.0655` n `67`; fx avg `0.0443` n `6`; index avg `-0.1725` n `23`; metal avg `-0.9695` n `18`; unknown avg `-2.0788` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
