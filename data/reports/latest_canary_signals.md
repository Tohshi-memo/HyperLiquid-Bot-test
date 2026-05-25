# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T11:22:19.376108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0835` n `12`; crypto_alt avg `-0.046` n `228`; crypto_major avg `-0.1019` n `8`; equity avg `0.059` n `67`; fx avg `-0.0004` n `6`; index avg `0.0218` n `23`; metal avg `0.1411` n `18`; unknown avg `0.8114` n `397`
- 1h: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.0325` n `228`; crypto_major avg `-0.1675` n `8`; equity avg `0.075` n `67`; fx avg `0.0205` n `6`; index avg `0.0256` n `23`; metal avg `0.0228` n `18`; unknown avg `0.7908` n `397`
- 4h: commodity avg `-0.4253` n `12`; crypto_alt avg `0.6177` n `228`; crypto_major avg `0.3312` n `8`; equity avg `0.3888` n `67`; fx avg `0.0296` n `6`; index avg `0.1544` n `23`; metal avg `0.5888` n `18`; unknown avg `0.8866` n `397`
- 24h: commodity avg `-0.1815` n `12`; crypto_alt avg `0.6198` n `228`; crypto_major avg `-0.2591` n `8`; equity avg `0.6415` n `67`; fx avg `0.0065` n `6`; index avg `0.0918` n `23`; metal avg `0.7895` n `18`; unknown avg `1.6622` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
