# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T21:12:12.745587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.31` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0231` n `12`; crypto_alt avg `-0.0851` n `230`; crypto_major avg `-0.0237` n `8`; equity avg `-0.1035` n `94`; fx avg `0.0185` n `6`; index avg `-0.0132` n `25`; metal avg `-0.0052` n `20`; unknown avg `-0.172` n `768`
- 1h: commodity avg `-0.0405` n `12`; crypto_alt avg `0.12` n `230`; crypto_major avg `0.1539` n `8`; equity avg `-0.0793` n `94`; fx avg `0.0069` n `6`; index avg `-0.021` n `25`; metal avg `0.0031` n `20`; unknown avg `-0.0225` n `768`
- 4h: commodity avg `0.2102` n `12`; crypto_alt avg `0.0486` n `230`; crypto_major avg `-0.1621` n `8`; equity avg `0.5133` n `94`; fx avg `0.0262` n `6`; index avg `0.1617` n `25`; metal avg `0.3959` n `20`; unknown avg `-0.2945` n `768`
- 24h: commodity avg `0.1718` n `12`; crypto_alt avg `0.4989` n `230`; crypto_major avg `0.6387` n `8`; equity avg `-0.5967` n `93`; fx avg `0.217` n `6`; index avg `-0.151` n `25`; metal avg `0.1563` n `20`; unknown avg `0.1359` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
