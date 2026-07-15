# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T20:22:31.266950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.52` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0306` n `12`; crypto_alt avg `0.2593` n `230`; crypto_major avg `0.2138` n `8`; equity avg `-0.0013` n `94`; fx avg `-0.0067` n `6`; index avg `-0.0002` n `25`; metal avg `0.0071` n `20`; unknown avg `0.0437` n `768`
- 1h: commodity avg `0.0609` n `12`; crypto_alt avg `0.3126` n `230`; crypto_major avg `0.2012` n `8`; equity avg `0.3606` n `94`; fx avg `-0.0058` n `6`; index avg `0.065` n `25`; metal avg `-0.0136` n `20`; unknown avg `-0.0892` n `768`
- 4h: commodity avg `0.2557` n `12`; crypto_alt avg `0.2781` n `230`; crypto_major avg `-0.0626` n `8`; equity avg `1.1894` n `94`; fx avg `0.0457` n `6`; index avg `0.2643` n `25`; metal avg `0.3945` n `20`; unknown avg `-0.277` n `768`
- 24h: commodity avg `0.101` n `12`; crypto_alt avg `0.7211` n `230`; crypto_major avg `0.8844` n `8`; equity avg `-0.4625` n `93`; fx avg `0.2045` n `6`; index avg `-0.1275` n `25`; metal avg `0.1435` n `20`; unknown avg `0.1311` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
