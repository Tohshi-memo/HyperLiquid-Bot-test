# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T05:52:15.071480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0446` n `12`; crypto_alt avg `0.0471` n `228`; crypto_major avg `-0.0274` n `8`; equity avg `-0.0472` n `66`; fx avg `0.0057` n `6`; index avg `-0.0127` n `23`; metal avg `-0.161` n `18`; unknown avg `-0.5306` n `384`
- 1h: commodity avg `0.0361` n `12`; crypto_alt avg `0.7989` n `228`; crypto_major avg `0.576` n `8`; equity avg `0.1053` n `66`; fx avg `-0.0175` n `6`; index avg `0.1111` n `23`; metal avg `0.3287` n `18`; unknown avg `0.0461` n `384`
- 4h: commodity avg `0.1967` n `12`; crypto_alt avg `1.0273` n `228`; crypto_major avg `0.7358` n `8`; equity avg `0.064` n `66`; fx avg `0.0237` n `6`; index avg `-0.0445` n `23`; metal avg `0.1042` n `18`; unknown avg `-0.2667` n `384`
- 24h: commodity avg `0.5668` n `12`; crypto_alt avg `-0.1254` n `228`; crypto_major avg `-0.1713` n `8`; equity avg `0.2497` n `66`; fx avg `-0.141` n `6`; index avg `-0.4721` n `23`; metal avg `-1.56` n `18`; unknown avg `1.0439` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0449`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0421`, n `668`, weak_sample_signal
