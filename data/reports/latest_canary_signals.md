# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T00:57:17.582773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0919` n `12`; crypto_alt avg `-0.1488` n `230`; crypto_major avg `-0.0717` n `8`; equity avg `-0.0464` n `107`; fx avg `-0.0505` n `6`; index avg `-0.0336` n `25`; metal avg `-0.0581` n `20`; unknown avg `0.0157` n `780`
- 1h: commodity avg `0.1696` n `12`; crypto_alt avg `-0.3464` n `230`; crypto_major avg `-0.3207` n `8`; equity avg `-0.9492` n `107`; fx avg `-0.0886` n `6`; index avg `-0.1943` n `25`; metal avg `-0.0322` n `20`; unknown avg `0.2587` n `780`
- 4h: commodity avg `0.2229` n `12`; crypto_alt avg `-0.5473` n `230`; crypto_major avg `-0.7244` n `8`; equity avg `-0.4863` n `107`; fx avg `-0.0384` n `6`; index avg `-0.1196` n `25`; metal avg `-0.0443` n `20`; unknown avg `0.352` n `780`
- 24h: commodity avg `0.1524` n `12`; crypto_alt avg `0.1615` n `230`; crypto_major avg `-0.0265` n `8`; equity avg `1.1116` n `107`; fx avg `-0.0443` n `6`; index avg `0.0906` n `25`; metal avg `-0.179` n `20`; unknown avg `0.0603` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
