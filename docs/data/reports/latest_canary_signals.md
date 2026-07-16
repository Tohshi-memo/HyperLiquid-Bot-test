# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T20:31:29.839088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0292` n `12`; crypto_alt avg `-0.0435` n `230`; crypto_major avg `-0.0922` n `8`; equity avg `-0.0484` n `94`; fx avg `0.0126` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0227` n `20`; unknown avg `-0.0438` n `768`
- 1h: commodity avg `0.0446` n `12`; crypto_alt avg `-0.0324` n `230`; crypto_major avg `-0.1508` n `8`; equity avg `-0.0574` n `94`; fx avg `0.0025` n `6`; index avg `0.0466` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.1557` n `768`
- 4h: commodity avg `0.0729` n `12`; crypto_alt avg `-0.653` n `230`; crypto_major avg `-0.9319` n `8`; equity avg `-0.6356` n `94`; fx avg `0.0105` n `6`; index avg `-0.125` n `25`; metal avg `-0.2721` n `20`; unknown avg `-0.1725` n `768`
- 24h: commodity avg `-0.3261` n `12`; crypto_alt avg `-1.1418` n `230`; crypto_major avg `-2.1523` n `8`; equity avg `-3.8972` n `94`; fx avg `-0.1486` n `6`; index avg `-0.5487` n `25`; metal avg `-0.8778` n `20`; unknown avg `-0.3737` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
