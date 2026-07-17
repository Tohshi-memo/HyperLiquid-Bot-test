# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T20:22:29.577364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0177` n `12`; crypto_alt avg `0.0343` n `230`; crypto_major avg `0.0471` n `8`; equity avg `0.0047` n `96`; fx avg `-0.0128` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0264` n `20`; unknown avg `-0.0163` n `769`
- 1h: commodity avg `0.0735` n `12`; crypto_alt avg `0.0479` n `230`; crypto_major avg `0.1744` n `8`; equity avg `-0.151` n `96`; fx avg `-0.0264` n `6`; index avg `-0.0279` n `25`; metal avg `0.033` n `20`; unknown avg `-0.1316` n `769`
- 4h: commodity avg `0.1592` n `12`; crypto_alt avg `-0.0519` n `230`; crypto_major avg `0.4333` n `8`; equity avg `-0.6149` n `96`; fx avg `-0.0102` n `6`; index avg `-0.1042` n `25`; metal avg `-0.0651` n `20`; unknown avg `0.2363` n `769`
- 24h: commodity avg `0.7361` n `12`; crypto_alt avg `-1.2348` n `230`; crypto_major avg `-1.2711` n `8`; equity avg `-1.4396` n `94`; fx avg `0.0835` n `6`; index avg `-0.2864` n `25`; metal avg `-0.0115` n `20`; unknown avg `-0.042` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
