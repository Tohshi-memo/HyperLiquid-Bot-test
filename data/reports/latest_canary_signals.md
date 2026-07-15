# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T18:07:27.522175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.31` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0259` n `12`; crypto_alt avg `0.001` n `230`; crypto_major avg `-0.027` n `8`; equity avg `0.183` n `94`; fx avg `0.0012` n `6`; index avg `0.0401` n `25`; metal avg `0.053` n `20`; unknown avg `-0.034` n `768`
- 1h: commodity avg `0.0184` n `12`; crypto_alt avg `0.1977` n `230`; crypto_major avg `0.1603` n `8`; equity avg `0.7582` n `94`; fx avg `0.0169` n `6`; index avg `0.1869` n `25`; metal avg `0.3072` n `20`; unknown avg `-0.0919` n `768`
- 4h: commodity avg `0.0553` n `12`; crypto_alt avg `-0.5199` n `230`; crypto_major avg `-0.5621` n `8`; equity avg `-1.2414` n `93`; fx avg `0.1093` n `6`; index avg `-0.1338` n `25`; metal avg `-0.085` n `20`; unknown avg `-0.0109` n `768`
- 24h: commodity avg `0.0823` n `12`; crypto_alt avg `0.4981` n `230`; crypto_major avg `1.1971` n `8`; equity avg `-0.2756` n `93`; fx avg `0.2179` n `6`; index avg `-0.1505` n `25`; metal avg `0.0253` n `20`; unknown avg `0.2939` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
