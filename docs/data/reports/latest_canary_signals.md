# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T22:22:25.665453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `0.0934` n `228`; crypto_major avg `0.1699` n `8`; equity avg `-0.0489` n `78`; fx avg `-0.0178` n `6`; index avg `-0.0075` n `23`; metal avg `0.0042` n `18`; unknown avg `0.5751` n `702`
- 1h: commodity avg `0.033` n `12`; crypto_alt avg `0.0961` n `228`; crypto_major avg `0.0167` n `8`; equity avg `-0.0837` n `78`; fx avg `0.0279` n `6`; index avg `-0.0754` n `23`; metal avg `-0.0212` n `18`; unknown avg `0.5306` n `702`
- 4h: commodity avg `-0.0299` n `12`; crypto_alt avg `-0.9375` n `228`; crypto_major avg `-0.5688` n `8`; equity avg `-0.2254` n `78`; fx avg `-0.0666` n `6`; index avg `-0.0602` n `23`; metal avg `-0.0682` n `18`; unknown avg `1.0901` n `694`
- 24h: commodity avg `0.2005` n `12`; crypto_alt avg `-0.074` n `228`; crypto_major avg `-1.1315` n `8`; equity avg `-0.0598` n `78`; fx avg `-0.1359` n `6`; index avg `-0.081` n `23`; metal avg `-0.1902` n `18`; unknown avg `0.936` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
