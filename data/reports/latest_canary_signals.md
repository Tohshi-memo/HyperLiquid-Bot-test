# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T21:59:13.546835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1147` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.5155` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0316` n `12`; crypto_alt avg `-0.1539` n `229`; crypto_major avg `0.0348` n `8`; equity avg `-0.0372` n `91`; fx avg `-0.0028` n `6`; index avg `0.004` n `25`; metal avg `0.0075` n `20`; unknown avg `-0.0128` n `763`
- 1h: commodity avg `0.037` n `12`; crypto_alt avg `-0.4388` n `229`; crypto_major avg `-0.4067` n `8`; equity avg `-0.3252` n `91`; fx avg `-0.0121` n `6`; index avg `-0.0204` n `25`; metal avg `0.0425` n `20`; unknown avg `-0.0557` n `763`
- 4h: commodity avg `0.4519` n `12`; crypto_alt avg `-1.7297` n `229`; crypto_major avg `-1.6628` n `8`; equity avg `-0.9905` n `91`; fx avg `-0.0196` n `6`; index avg `-0.1473` n `25`; metal avg `-0.3877` n `20`; unknown avg `1.0812` n `761`
- 24h: commodity avg `0.9396` n `12`; crypto_alt avg `-3.2027` n `229`; crypto_major avg `-2.446` n `8`; equity avg `-3.5654` n `91`; fx avg `-0.2912` n `6`; index avg `-0.638` n `25`; metal avg `-0.5762` n `20`; unknown avg `-0.4783` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
