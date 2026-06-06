# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T19:07:26.187566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.123` n `12`; crypto_alt avg `0.5024` n `228`; crypto_major avg `0.3273` n `8`; equity avg `0.1088` n `74`; fx avg `-0.0117` n `6`; index avg `0.0805` n `23`; metal avg `0.0163` n `18`; unknown avg `0.0706` n `515`
- 1h: commodity avg `-0.0853` n `12`; crypto_alt avg `0.7396` n `228`; crypto_major avg `0.3974` n `8`; equity avg `0.1624` n `74`; fx avg `-0.0715` n `6`; index avg `0.0122` n `23`; metal avg `0.0101` n `18`; unknown avg `0.1224` n `515`
- 4h: commodity avg `0.0693` n `12`; crypto_alt avg `0.022` n `228`; crypto_major avg `-0.1766` n `8`; equity avg `0.0642` n `74`; fx avg `0.1159` n `6`; index avg `0.0076` n `23`; metal avg `0.1455` n `18`; unknown avg `-3.0584` n `515`
- 24h: commodity avg `0.3744` n `12`; crypto_alt avg `1.6615` n `228`; crypto_major avg `1.0038` n `8`; equity avg `-1.0108` n `74`; fx avg `0.0894` n `6`; index avg `-0.1407` n `23`; metal avg `-0.558` n `18`; unknown avg `1.19` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
