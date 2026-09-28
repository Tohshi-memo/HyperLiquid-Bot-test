# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T04:52:27.711343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2497` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0487` n `12`; crypto_alt avg `0.2601` n `234`; crypto_major avg `0.0941` n `8`; equity avg `-0.0236` n `141`; fx avg `0.0037` n `6`; index avg `-0.0071` n `26`; metal avg `-0.0164` n `20`; unknown avg `0.5955` n `962`
- 1h: commodity avg `0.092` n `12`; crypto_alt avg `0.2772` n `234`; crypto_major avg `0.1646` n `8`; equity avg `0.063` n `141`; fx avg `0.0091` n `6`; index avg `0.0126` n `26`; metal avg `-0.0202` n `20`; unknown avg `0.5519` n `952`
- 4h: commodity avg `0.2155` n `12`; crypto_alt avg `-2.1796` n `234`; crypto_major avg `-1.3868` n `8`; equity avg `-1.1108` n `141`; fx avg `0.0091` n `6`; index avg `-0.1371` n `26`; metal avg `-0.3449` n `20`; unknown avg `179.589` n `936`
- 24h: commodity avg `-0.3291` n `12`; crypto_alt avg `-0.4099` n `234`; crypto_major avg `-0.8769` n `8`; equity avg `-1.3838` n `141`; fx avg `0.0534` n `6`; index avg `-0.1453` n `26`; metal avg `-0.7003` n `20`; unknown avg `8.2477` n `811`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
