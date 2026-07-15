# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T21:22:30.336277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0213` n `12`; crypto_alt avg `0.0701` n `230`; crypto_major avg `0.0831` n `8`; equity avg `-0.0106` n `94`; fx avg `-0.0045` n `6`; index avg `0.0002` n `25`; metal avg `-0.0107` n `20`; unknown avg `-0.1591` n `768`
- 1h: commodity avg `-0.0313` n `12`; crypto_alt avg `-0.0686` n `230`; crypto_major avg `0.0231` n `8`; equity avg `-0.0887` n `94`; fx avg `0.0091` n `6`; index avg `-0.0207` n `25`; metal avg `-0.0148` n `20`; unknown avg `0.2025` n `768`
- 4h: commodity avg `0.1647` n `12`; crypto_alt avg `0.1741` n `230`; crypto_major avg `-0.0752` n `8`; equity avg `0.266` n `94`; fx avg `0.0226` n `6`; index avg `0.1268` n `25`; metal avg `0.3639` n `20`; unknown avg `-0.3404` n `768`
- 24h: commodity avg `0.1152` n `12`; crypto_alt avg `0.5386` n `230`; crypto_major avg `0.6336` n `8`; equity avg `-0.6117` n `93`; fx avg `0.2209` n `6`; index avg `-0.1579` n `25`; metal avg `0.134` n `20`; unknown avg `0.0693` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
