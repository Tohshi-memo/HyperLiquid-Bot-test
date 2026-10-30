# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T02:37:28.322376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1395` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0906` n `13`; crypto_alt avg `0.5047` n `238`; crypto_major avg `0.5827` n `8`; equity avg `0.2139` n `156`; fx avg `0.0176` n `6`; index avg `0.0225` n `27`; metal avg `-0.0128` n `20`; unknown avg `0.9274` n `1260`
- 1h: commodity avg `0.0196` n `13`; crypto_alt avg `0.5954` n `238`; crypto_major avg `1.0066` n `8`; equity avg `0.2385` n `156`; fx avg `0.016` n `6`; index avg `0.0099` n `27`; metal avg `0.0012` n `20`; unknown avg `4.4129` n `1254`
- 4h: commodity avg `0.1388` n `13`; crypto_alt avg `-2.2381` n `238`; crypto_major avg `-1.2971` n `8`; equity avg `-0.6179` n `156`; fx avg `0.008` n `6`; index avg `-0.1576` n `27`; metal avg `-0.277` n `20`; unknown avg `7.3254` n `1240`
- 24h: commodity avg `-0.0725` n `13`; crypto_alt avg `-4.6302` n `238`; crypto_major avg `-0.6803` n `8`; equity avg `-2.6168` n `155`; fx avg `0.1887` n `6`; index avg `-0.2327` n `27`; metal avg `-0.6283` n `20`; unknown avg `31.0643` n `988`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
