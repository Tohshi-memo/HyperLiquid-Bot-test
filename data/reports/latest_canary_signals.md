# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T14:22:17.110471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.4479` n `228`; crypto_major avg `-0.4568` n `8`; equity avg `-0.204` n `67`; fx avg `-0.0157` n `6`; index avg `-0.0792` n `23`; metal avg `-0.2968` n `18`; unknown avg `-0.0921` n `386`
- 1h: commodity avg `0.4755` n `12`; crypto_alt avg `-1.1977` n `228`; crypto_major avg `-0.8182` n `8`; equity avg `-0.5849` n `67`; fx avg `-0.0325` n `6`; index avg `-0.0631` n `23`; metal avg `-0.8233` n `18`; unknown avg `-0.1426` n `386`
- 4h: commodity avg `-0.4645` n `12`; crypto_alt avg `-0.1994` n `228`; crypto_major avg `0.0094` n `8`; equity avg `-0.0685` n `67`; fx avg `-0.0455` n `6`; index avg `0.149` n `23`; metal avg `-1.1409` n `18`; unknown avg `0.151` n `386`
- 24h: commodity avg `-1.3633` n `12`; crypto_alt avg `1.8508` n `228`; crypto_major avg `0.6148` n `8`; equity avg `1.2278` n `67`; fx avg `0.1073` n `6`; index avg `1.0453` n `23`; metal avg `0.0123` n `18`; unknown avg `1.0118` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0445`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0416`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0401`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0399`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0379`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0379`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0344`, n `668`, weak_sample_signal
