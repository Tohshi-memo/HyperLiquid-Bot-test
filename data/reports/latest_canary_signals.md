# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T19:17:01.242966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0348` n `12`; crypto_alt avg `-0.0261` n `230`; crypto_major avg `0.0193` n `8`; equity avg `-0.0044` n `114`; fx avg `0.0012` n `6`; index avg `0.0015` n `25`; metal avg `0.0016` n `20`; unknown avg `0.0198` n `791`
- 1h: commodity avg `0.0513` n `12`; crypto_alt avg `0.0351` n `230`; crypto_major avg `0.085` n `8`; equity avg `0.0024` n `114`; fx avg `0.0134` n `6`; index avg `0.0128` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0758` n `791`
- 4h: commodity avg `0.0716` n `12`; crypto_alt avg `-0.193` n `230`; crypto_major avg `0.0373` n `8`; equity avg `0.0673` n `114`; fx avg `0.0014` n `6`; index avg `0.0092` n `25`; metal avg `0.0234` n `20`; unknown avg `-0.074` n `791`
- 24h: commodity avg `0.0619` n `12`; crypto_alt avg `-0.3125` n `230`; crypto_major avg `0.025` n `8`; equity avg `0.2705` n `114`; fx avg `-0.0018` n `6`; index avg `0.02` n `25`; metal avg `0.0548` n `20`; unknown avg `0.0909` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.215`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
