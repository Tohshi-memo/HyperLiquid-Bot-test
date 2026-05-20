# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T00:07:17.393066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0949` n `12`; crypto_alt avg `0.0581` n `228`; crypto_major avg `-0.2345` n `8`; equity avg `-0.358` n `66`; fx avg `0.0377` n `6`; index avg `-0.2644` n `23`; metal avg `-0.2249` n `18`; unknown avg `-0.0989` n `383`
- 1h: commodity avg `-0.1864` n `12`; crypto_alt avg `0.3217` n `228`; crypto_major avg `-0.03` n `8`; equity avg `-0.1598` n `66`; fx avg `0.0304` n `6`; index avg `-0.0827` n `23`; metal avg `-0.053` n `18`; unknown avg `-0.1368` n `383`
- 4h: commodity avg `-0.2829` n `12`; crypto_alt avg `-0.1397` n `228`; crypto_major avg `-0.3188` n `8`; equity avg `-0.2488` n `66`; fx avg `-0.0089` n `6`; index avg `-0.1912` n `23`; metal avg `0.1371` n `18`; unknown avg `-0.4118` n `383`
- 24h: commodity avg `0.7627` n `12`; crypto_alt avg `-1.1513` n `228`; crypto_major avg `-0.9869` n `8`; equity avg `-0.5011` n `66`; fx avg `0.0217` n `6`; index avg `-0.7677` n `23`; metal avg `-3.0608` n `18`; unknown avg `0.6603` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
