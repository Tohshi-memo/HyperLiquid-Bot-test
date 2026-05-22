# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T12:33:07.744621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `0.0513` n `228`; crypto_major avg `0.1315` n `8`; equity avg `0.0297` n `67`; fx avg `0.0048` n `6`; index avg `0.0244` n `23`; metal avg `-0.1532` n `18`; unknown avg `-0.0025` n `386`
- 1h: commodity avg `-0.9002` n `12`; crypto_alt avg `0.341` n `228`; crypto_major avg `0.6429` n `8`; equity avg `0.2624` n `67`; fx avg `-0.0057` n `6`; index avg `0.1302` n `23`; metal avg `-0.4171` n `18`; unknown avg `0.1694` n `386`
- 4h: commodity avg `-1.1044` n `12`; crypto_alt avg `0.3868` n `228`; crypto_major avg `0.7797` n `8`; equity avg `-0.2888` n `67`; fx avg `-0.0399` n `6`; index avg `-0.0882` n `23`; metal avg `-0.3119` n `18`; unknown avg `-0.4079` n `386`
- 24h: commodity avg `-1.7045` n `12`; crypto_alt avg `2.7956` n `228`; crypto_major avg `1.6307` n `8`; equity avg `1.4488` n `67`; fx avg `0.0986` n `6`; index avg `0.9169` n `23`; metal avg `0.4671` n `18`; unknown avg `1.0313` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0427`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0405`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0373`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.037`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0355`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0342`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0325`, n `668`, weak_sample_signal
