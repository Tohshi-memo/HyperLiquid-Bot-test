# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T05:37:25.909902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0388` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0061` n `13`; crypto_alt avg `0.2881` n `239`; crypto_major avg `0.1652` n `8`; equity avg `0.014` n `165`; fx avg `0.0085` n `6`; index avg `-0.0223` n `27`; metal avg `-0.0473` n `20`; unknown avg `159.0222` n `1262`
- 1h: commodity avg `-0.0335` n `13`; crypto_alt avg `0.4412` n `239`; crypto_major avg `0.3812` n `8`; equity avg `-0.4536` n `165`; fx avg `-0.0165` n `6`; index avg `-0.0383` n `27`; metal avg `-0.0931` n `20`; unknown avg `79.8735` n `1250`
- 4h: commodity avg `-0.018` n `13`; crypto_alt avg `-1.4087` n `239`; crypto_major avg `-1.145` n `8`; equity avg `-0.9938` n `165`; fx avg `0.0212` n `6`; index avg `-0.1062` n `27`; metal avg `-0.5172` n `20`; unknown avg `2.298` n `1238`
- 24h: commodity avg `-0.0978` n `13`; crypto_alt avg `-3.2604` n `239`; crypto_major avg `-2.7789` n `8`; equity avg `-6.2993` n `165`; fx avg `0.0202` n `6`; index avg `-0.5591` n `27`; metal avg `-1.9881` n `20`; unknown avg `234.2711` n `1167`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
