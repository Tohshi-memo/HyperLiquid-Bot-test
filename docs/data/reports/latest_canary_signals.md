# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T10:52:27.915558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.0636` n `230`; crypto_major avg `0.0285` n `8`; equity avg `-0.0022` n `114`; fx avg `0.032` n `6`; index avg `0.001` n `25`; metal avg `0.0021` n `20`; unknown avg `0.0084` n `791`
- 1h: commodity avg `-0.0416` n `12`; crypto_alt avg `-0.026` n `230`; crypto_major avg `-0.0028` n `8`; equity avg `-0.0223` n `114`; fx avg `0.0229` n `6`; index avg `0.0044` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.0204` n `791`
- 4h: commodity avg `-0.1516` n `12`; crypto_alt avg `-0.0438` n `230`; crypto_major avg `-0.2022` n `8`; equity avg `0.0041` n `114`; fx avg `0.0223` n `6`; index avg `-0.0008` n `25`; metal avg `0.0011` n `20`; unknown avg `-0.0187` n `791`
- 24h: commodity avg `0.007` n `12`; crypto_alt avg `1.0404` n `230`; crypto_major avg `0.0971` n `8`; equity avg `-0.5376` n `114`; fx avg `0.1581` n `6`; index avg `-0.1352` n `25`; metal avg `0.2166` n `20`; unknown avg `-0.1323` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2157`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1828`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
