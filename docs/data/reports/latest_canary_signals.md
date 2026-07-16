# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T16:22:26.655396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6346` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `-0.0315` n `230`; crypto_major avg `-0.1262` n `8`; equity avg `-0.3011` n `94`; fx avg `0.0009` n `6`; index avg `-0.0773` n `25`; metal avg `-0.0906` n `20`; unknown avg `-0.0616` n `768`
- 1h: commodity avg `0.0417` n `12`; crypto_alt avg `0.0909` n `230`; crypto_major avg `-0.2143` n `8`; equity avg `-0.6027` n `94`; fx avg `-0.0285` n `6`; index avg `-0.0767` n `25`; metal avg `-0.1456` n `20`; unknown avg `-0.1316` n `768`
- 4h: commodity avg `-0.3827` n `12`; crypto_alt avg `0.4624` n `230`; crypto_major avg `-0.0886` n `8`; equity avg `-1.7232` n `94`; fx avg `-0.0492` n `6`; index avg `-0.0721` n `25`; metal avg `-0.2227` n `20`; unknown avg `-0.1676` n `768`
- 24h: commodity avg `-0.0453` n `12`; crypto_alt avg `-0.3405` n `230`; crypto_major avg `-1.3591` n `8`; equity avg `-2.3065` n `94`; fx avg `-0.1054` n `6`; index avg `-0.1913` n `25`; metal avg `-0.2738` n `20`; unknown avg `-0.2212` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
