# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T17:37:26.394216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0617` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0217` n `12`; crypto_alt avg `0.1006` n `228`; crypto_major avg `0.2977` n `8`; equity avg `0.1054` n `86`; fx avg `0.0024` n `6`; index avg `0.0152` n `23`; metal avg `-0.0161` n `20`; unknown avg `0.2777` n `765`
- 1h: commodity avg `0.0428` n `12`; crypto_alt avg `0.444` n `228`; crypto_major avg `0.8855` n `8`; equity avg `0.0253` n `86`; fx avg `-0.0046` n `6`; index avg `0.0008` n `23`; metal avg `0.0006` n `20`; unknown avg `0.3197` n `765`
- 4h: commodity avg `0.2618` n `12`; crypto_alt avg `-1.368` n `228`; crypto_major avg `-1.288` n `8`; equity avg `-1.7106` n `86`; fx avg `0.0643` n `6`; index avg `-0.2263` n `23`; metal avg `0.0865` n `20`; unknown avg `1.0072` n `765`
- 24h: commodity avg `0.3662` n `12`; crypto_alt avg `1.5238` n `228`; crypto_major avg `1.3255` n `8`; equity avg `0.4281` n `86`; fx avg `0.0792` n `6`; index avg `0.4941` n `23`; metal avg `0.6609` n `20`; unknown avg `0.5121` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
