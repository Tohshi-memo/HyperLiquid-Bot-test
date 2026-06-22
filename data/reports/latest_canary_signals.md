# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T07:22:30.863256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0` n `12`; crypto_alt avg `0.3132` n `228`; crypto_major avg `0.3656` n `8`; equity avg `0.1016` n `79`; fx avg `0.0148` n `6`; index avg `0.0073` n `23`; metal avg `0.0141` n `18`; unknown avg `0.0469` n `701`
- 1h: commodity avg `0.0907` n `12`; crypto_alt avg `0.3605` n `228`; crypto_major avg `0.4773` n `8`; equity avg `0.3477` n `79`; fx avg `0.0437` n `6`; index avg `0.0419` n `23`; metal avg `0.0601` n `18`; unknown avg `-0.0253` n `701`
- 4h: commodity avg `-0.0526` n `12`; crypto_alt avg `0.1529` n `228`; crypto_major avg `0.1889` n `8`; equity avg `0.3932` n `79`; fx avg `0.009` n `6`; index avg `0.0117` n `23`; metal avg `0.438` n `18`; unknown avg `0.5477` n `669`
- 24h: commodity avg `-0.2297` n `12`; crypto_alt avg `0.3213` n `228`; crypto_major avg `-0.1339` n `8`; equity avg `-0.2139` n `79`; fx avg `0.0347` n `6`; index avg `0.0074` n `23`; metal avg `0.4942` n `18`; unknown avg `-0.3706` n `643`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
