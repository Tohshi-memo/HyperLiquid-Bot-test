# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T00:37:26.616423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `12`; crypto_alt avg `0.2367` n `234`; crypto_major avg `0.092` n `8`; equity avg `0.0206` n `140`; fx avg `0.0015` n `6`; index avg `-0.0117` n `26`; metal avg `0.0002` n `20`; unknown avg `1.0927` n `943`
- 1h: commodity avg `0.0447` n `12`; crypto_alt avg `0.4378` n `234`; crypto_major avg `-0.0976` n `8`; equity avg `0.0597` n `140`; fx avg `0.0083` n `6`; index avg `-0.0111` n `26`; metal avg `0.0067` n `20`; unknown avg `0.0966` n `935`
- 4h: commodity avg `0.1034` n `12`; crypto_alt avg `0.2822` n `234`; crypto_major avg `-0.3799` n `8`; equity avg `0.0299` n `140`; fx avg `0.01` n `6`; index avg `-0.0032` n `26`; metal avg `0.0004` n `20`; unknown avg `0.2778` n `911`
- 24h: commodity avg `-0.0103` n `12`; crypto_alt avg `1.0673` n `234`; crypto_major avg `-0.4836` n `8`; equity avg `-0.0146` n `140`; fx avg `-0.0753` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.2354` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
