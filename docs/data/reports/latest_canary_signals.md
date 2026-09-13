# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T10:07:30.659530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1576` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `0.0753` n `233`; crypto_major avg `0.0032` n `8`; equity avg `0.0012` n `136`; fx avg `0.0013` n `6`; index avg `0.0018` n `27`; metal avg `-0.0049` n `20`; unknown avg `0.0227` n `836`
- 1h: commodity avg `0.0152` n `12`; crypto_alt avg `-0.2913` n `233`; crypto_major avg `-0.5963` n `8`; equity avg `-0.4826` n `136`; fx avg `0.008` n `6`; index avg `-0.0816` n `27`; metal avg `-0.0247` n `20`; unknown avg `-0.0141` n `830`
- 4h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.9772` n `233`; crypto_major avg `-1.3072` n `8`; equity avg `-0.9501` n `136`; fx avg `0.0065` n `6`; index avg `-0.1496` n `26`; metal avg `-0.052` n `20`; unknown avg `-0.2356` n `830`
- 24h: commodity avg `0.1129` n `12`; crypto_alt avg `-0.4011` n `233`; crypto_major avg `-1.7319` n `8`; equity avg `-1.5929` n `136`; fx avg `-0.0005` n `6`; index avg `-0.25` n `26`; metal avg `-0.0237` n `20`; unknown avg `-0.0052` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0866`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.079`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0748`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0741`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `669`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0648`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0633`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.057`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0557`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0554`, n `669`, weak_sample_signal
