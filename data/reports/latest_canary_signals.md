# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T19:07:28.049836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.0333` n `230`; crypto_major avg `-0.1125` n `8`; equity avg `0.0934` n `94`; fx avg `0.007` n `6`; index avg `0.0368` n `25`; metal avg `0.0032` n `20`; unknown avg `0.0242` n `768`
- 1h: commodity avg `0.101` n `12`; crypto_alt avg `-0.1545` n `230`; crypto_major avg `-0.2548` n `8`; equity avg `-0.3122` n `94`; fx avg `-0.0012` n `6`; index avg `-0.0385` n `25`; metal avg `0.1181` n `20`; unknown avg `0.019` n `768`
- 4h: commodity avg `0.258` n `12`; crypto_alt avg `-0.479` n `230`; crypto_major avg `-0.7751` n `8`; equity avg `-0.2348` n `94`; fx avg `0.052` n `6`; index avg `0.0772` n `25`; metal avg `0.2045` n `20`; unknown avg `-0.017` n `768`
- 24h: commodity avg `0.0598` n `12`; crypto_alt avg `0.5085` n `230`; crypto_major avg `0.7804` n `8`; equity avg `-0.4101` n `93`; fx avg `0.2134` n `6`; index avg `-0.1368` n `25`; metal avg `0.2045` n `20`; unknown avg `0.3266` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
