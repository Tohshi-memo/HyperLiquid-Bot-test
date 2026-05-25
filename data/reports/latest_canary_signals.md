# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T02:52:15.580346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.0472` n `228`; crypto_major avg `0.0658` n `8`; equity avg `0.0393` n `67`; fx avg `-0.0249` n `6`; index avg `0.0236` n `23`; metal avg `-0.0549` n `18`; unknown avg `-0.0716` n `396`
- 1h: commodity avg `-0.1241` n `12`; crypto_alt avg `-0.0226` n `228`; crypto_major avg `-0.0508` n `8`; equity avg `0.0003` n `67`; fx avg `-0.0333` n `6`; index avg `0.0061` n `23`; metal avg `-0.1074` n `18`; unknown avg `0.0949` n `396`
- 4h: commodity avg `0.1113` n `12`; crypto_alt avg `0.5346` n `228`; crypto_major avg `0.0416` n `8`; equity avg `0.2414` n `67`; fx avg `-0.1729` n `6`; index avg `0.1429` n `23`; metal avg `-0.0297` n `18`; unknown avg `0.2412` n `396`
- 24h: commodity avg `0.1393` n `12`; crypto_alt avg `-1.3047` n `228`; crypto_major avg `-0.1473` n `8`; equity avg `0.3041` n `67`; fx avg `-0.063` n `6`; index avg `-0.3007` n `23`; metal avg `0.5723` n `18`; unknown avg `-0.7537` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
