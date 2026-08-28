# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T16:07:32.877847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0353` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0174` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `-0.4184` n `231`; crypto_major avg `-0.1758` n `8`; equity avg `-0.1515` n `127`; fx avg `-0.0092` n `6`; index avg `-0.0272` n `26`; metal avg `-0.2269` n `20`; unknown avg `-0.068` n `793`
- 1h: commodity avg `-0.0766` n `12`; crypto_alt avg `-1.4079` n `231`; crypto_major avg `-1.1837` n `8`; equity avg `-0.958` n `127`; fx avg `-0.0075` n `6`; index avg `-0.1663` n `26`; metal avg `-0.4814` n `20`; unknown avg `3.2544` n `793`
- 4h: commodity avg `0.0582` n `12`; crypto_alt avg `-1.4965` n `231`; crypto_major avg `-1.0994` n `8`; equity avg `-1.1092` n `127`; fx avg `-0.0193` n `6`; index avg `-0.0641` n `26`; metal avg `-0.4242` n `20`; unknown avg `-0.3963` n `792`
- 24h: commodity avg `-0.0522` n `12`; crypto_alt avg `-2.6417` n `231`; crypto_major avg `-2.2155` n `8`; equity avg `-1.6868` n `127`; fx avg `-0.0788` n `6`; index avg `-0.062` n `26`; metal avg `0.0915` n `20`; unknown avg `-0.0375` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
