# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T17:37:24.982169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2126` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0407` n `12`; crypto_alt avg `-0.0206` n `230`; crypto_major avg `-0.0874` n `8`; equity avg `-0.1071` n `112`; fx avg `-0.0025` n `6`; index avg `-0.0175` n `25`; metal avg `0.0069` n `20`; unknown avg `-0.0458` n `782`
- 1h: commodity avg `-0.0977` n `12`; crypto_alt avg `-0.3642` n `230`; crypto_major avg `-0.7327` n `8`; equity avg `0.0108` n `112`; fx avg `-0.0054` n `6`; index avg `-0.003` n `25`; metal avg `-0.0202` n `20`; unknown avg `0.1578` n `782`
- 4h: commodity avg `0.1856` n `12`; crypto_alt avg `-0.5675` n `230`; crypto_major avg `-1.3009` n `8`; equity avg `-0.1169` n `112`; fx avg `-0.0165` n `6`; index avg `-0.0883` n `25`; metal avg `-0.2217` n `20`; unknown avg `0.3735` n `782`
- 24h: commodity avg `0.3208` n `12`; crypto_alt avg `-0.6114` n `230`; crypto_major avg `-0.919` n `8`; equity avg `0.5898` n `112`; fx avg `-0.1507` n `6`; index avg `-0.0476` n `25`; metal avg `0.2455` n `20`; unknown avg `-0.1123` n `765`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
