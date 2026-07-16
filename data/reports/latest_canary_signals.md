# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T18:37:30.117263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3291` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0417` n `12`; crypto_alt avg `-0.2152` n `230`; crypto_major avg `-0.2693` n `8`; equity avg `-0.2323` n `94`; fx avg `-0.0064` n `6`; index avg `-0.0424` n `25`; metal avg `-0.1354` n `20`; unknown avg `-0.133` n `768`
- 1h: commodity avg `0.0257` n `12`; crypto_alt avg `-0.2256` n `230`; crypto_major avg `-0.2637` n `8`; equity avg `-0.0582` n `94`; fx avg `-0.0063` n `6`; index avg `-0.0492` n `25`; metal avg `-0.0958` n `20`; unknown avg `-0.1938` n `768`
- 4h: commodity avg `-0.2597` n `12`; crypto_alt avg `-0.729` n `230`; crypto_major avg `-1.5524` n `8`; equity avg `-1.3409` n `94`; fx avg `-0.0687` n `6`; index avg `-0.2233` n `25`; metal avg `-0.3445` n `20`; unknown avg `-0.0724` n `768`
- 24h: commodity avg `-0.3629` n `12`; crypto_alt avg `-1.2061` n `230`; crypto_major avg `-2.6064` n `8`; equity avg `-3.7076` n `94`; fx avg `-0.1685` n `6`; index avg `-0.5148` n `25`; metal avg `-0.9268` n `20`; unknown avg `-0.3842` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
