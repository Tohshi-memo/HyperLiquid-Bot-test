# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T02:52:37.238603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.2234` n `230`; crypto_major avg `-0.0383` n `8`; equity avg `-0.1701` n `114`; fx avg `-0.022` n `6`; index avg `-0.0132` n `25`; metal avg `0.0088` n `20`; unknown avg `0.0814` n `793`
- 1h: commodity avg `-0.0132` n `12`; crypto_alt avg `-0.5168` n `230`; crypto_major avg `-0.2394` n `8`; equity avg `-0.7674` n `114`; fx avg `-0.0157` n `6`; index avg `-0.1178` n `25`; metal avg `-0.0611` n `20`; unknown avg `0.1608` n `793`
- 4h: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.805` n `230`; crypto_major avg `-0.3613` n `8`; equity avg `-1.6413` n `114`; fx avg `-0.091` n `6`; index avg `-0.2688` n `25`; metal avg `-0.1614` n `20`; unknown avg `-0.0244` n `793`
- 24h: commodity avg `0.6027` n `12`; crypto_alt avg `-1.2482` n `230`; crypto_major avg `-0.1131` n `8`; equity avg `-1.0071` n `114`; fx avg `-0.052` n `6`; index avg `-0.2238` n `25`; metal avg `-0.1612` n `20`; unknown avg `0.0154` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
