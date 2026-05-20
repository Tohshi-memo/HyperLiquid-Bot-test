# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T15:07:21.870152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.035` n `12`; crypto_alt avg `-0.1186` n `228`; crypto_major avg `-0.1466` n `8`; equity avg `0.0455` n `66`; fx avg `0.0084` n `6`; index avg `0.0227` n `23`; metal avg `-0.1214` n `18`; unknown avg `-0.1041` n `384`
- 1h: commodity avg `-0.9715` n `12`; crypto_alt avg `0.8378` n `228`; crypto_major avg `0.4989` n `8`; equity avg `0.6493` n `66`; fx avg `-0.021` n `6`; index avg `0.4383` n `23`; metal avg `0.8622` n `18`; unknown avg `-0.1855` n `384`
- 4h: commodity avg `-0.8564` n `12`; crypto_alt avg `0.7895` n `228`; crypto_major avg `0.53` n `8`; equity avg `0.3615` n `66`; fx avg `-0.0237` n `6`; index avg `0.6809` n `23`; metal avg `0.2814` n `18`; unknown avg `1.0378` n `384`
- 24h: commodity avg `-1.454` n `12`; crypto_alt avg `2.1854` n `228`; crypto_major avg `1.6727` n `8`; equity avg `2.4748` n `66`; fx avg `-0.0861` n `6`; index avg `1.6026` n `23`; metal avg `1.2924` n `18`; unknown avg `0.8623` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
