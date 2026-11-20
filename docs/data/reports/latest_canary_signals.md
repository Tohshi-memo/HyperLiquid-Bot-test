# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T22:07:31.916740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.14` - Polymarket crypto volume is unusually high.
- 1h_crypto_metal_divergence: score `1.5353` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0296` n `13`; crypto_alt avg `0.1149` n `239`; crypto_major avg `0.0383` n `8`; equity avg `-0.1962` n `166`; fx avg `0.0069` n `6`; index avg `-0.0087` n `27`; metal avg `0.011` n `20`; unknown avg `-0.1885` n `1246`
- 1h: commodity avg `0.0169` n `13`; crypto_alt avg `1.4459` n `239`; crypto_major avg `1.6601` n `8`; equity avg `0.4797` n `166`; fx avg `0.0138` n `6`; index avg `0.0362` n `27`; metal avg `0.1248` n `20`; unknown avg `159.6868` n `1250`
- 4h: commodity avg `0.552` n `13`; crypto_alt avg `0.6014` n `239`; crypto_major avg `0.0388` n `8`; equity avg `-0.6357` n `166`; fx avg `-0.0129` n `6`; index avg `-0.1328` n `27`; metal avg `0.0553` n `20`; unknown avg `4.335` n `1210`
- 24h: commodity avg `0.2946` n `13`; crypto_alt avg `-4.5007` n `239`; crypto_major avg `-5.0196` n `8`; equity avg `-6.5411` n `166`; fx avg `0.0262` n `6`; index avg `-0.7257` n `27`; metal avg `-0.7961` n `20`; unknown avg `30.7327` n `1131`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
