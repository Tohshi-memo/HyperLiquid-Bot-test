# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T08:07:18.054221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2205` n `12`; crypto_alt avg `0.1498` n `228`; crypto_major avg `0.2864` n `8`; equity avg `0.2137` n `66`; fx avg `0.0023` n `6`; index avg `0.0687` n `23`; metal avg `0.0748` n `18`; unknown avg `0.0329` n `386`
- 1h: commodity avg `-0.2763` n `12`; crypto_alt avg `0.3991` n `228`; crypto_major avg `0.7292` n `8`; equity avg `0.3373` n `66`; fx avg `-0.0319` n `6`; index avg `0.136` n `23`; metal avg `0.0126` n `18`; unknown avg `1.7805` n `385`
- 4h: commodity avg `-0.0758` n `12`; crypto_alt avg `-0.0796` n `228`; crypto_major avg `0.3636` n `8`; equity avg `-0.0525` n `66`; fx avg `-0.0257` n `6`; index avg `-0.0462` n `23`; metal avg `-0.3876` n `18`; unknown avg `1.4997` n `374`
- 24h: commodity avg `-1.8601` n `12`; crypto_alt avg `2.6985` n `228`; crypto_major avg `3.6125` n `8`; equity avg `1.6864` n `66`; fx avg `0.0415` n `6`; index avg `1.4215` n `23`; metal avg `0.1502` n `18`; unknown avg `6.52` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
