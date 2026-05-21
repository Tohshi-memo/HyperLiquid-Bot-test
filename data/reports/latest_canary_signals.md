# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T08:22:15.244095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0569` n `12`; crypto_alt avg `-0.1004` n `228`; crypto_major avg `0.0247` n `8`; equity avg `0.0774` n `66`; fx avg `0.0304` n `6`; index avg `0.0718` n `23`; metal avg `0.1999` n `18`; unknown avg `-0.0071` n `386`
- 1h: commodity avg `-0.3991` n `12`; crypto_alt avg `0.439` n `228`; crypto_major avg `0.7325` n `8`; equity avg `0.5501` n `66`; fx avg `0.0452` n `6`; index avg `0.2725` n `23`; metal avg `0.3049` n `18`; unknown avg `1.314` n `385`
- 4h: commodity avg `-0.1576` n `12`; crypto_alt avg `0.018` n `228`; crypto_major avg `0.472` n `8`; equity avg `0.0201` n `66`; fx avg `-0.0008` n `6`; index avg `0.0398` n `23`; metal avg `-0.2404` n `18`; unknown avg `0.7878` n `374`
- 24h: commodity avg `-2.0413` n `12`; crypto_alt avg `2.729` n `228`; crypto_major avg `3.6992` n `8`; equity avg `1.8351` n `66`; fx avg `0.0784` n `6`; index avg `1.4144` n `23`; metal avg `0.3205` n `18`; unknown avg `5.69` n `374`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
