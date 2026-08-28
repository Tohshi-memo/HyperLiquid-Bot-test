# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T17:22:32.629262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.137` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.051` n `12`; crypto_alt avg `0.2876` n `231`; crypto_major avg `0.2111` n `8`; equity avg `0.0912` n `127`; fx avg `0.0033` n `6`; index avg `0.0208` n `26`; metal avg `0.0383` n `20`; unknown avg `0.0891` n `793`
- 1h: commodity avg `0.055` n `12`; crypto_alt avg `0.8369` n `231`; crypto_major avg `0.6592` n `8`; equity avg `0.0018` n `127`; fx avg `-0.0032` n `6`; index avg `0.0014` n `26`; metal avg `0.0608` n `20`; unknown avg `0.6528` n `793`
- 4h: commodity avg `0.0663` n `12`; crypto_alt avg `-1.3262` n `231`; crypto_major avg `-1.3271` n `8`; equity avg `-1.4982` n `127`; fx avg `-0.0144` n `6`; index avg `-0.1901` n `26`; metal avg `-0.6877` n `20`; unknown avg `3.4658` n `793`
- 24h: commodity avg `-0.1388` n `12`; crypto_alt avg `-3.6189` n `231`; crypto_major avg `-3.4362` n `8`; equity avg `-2.2606` n `127`; fx avg `-0.0817` n `6`; index avg `-0.2046` n `26`; metal avg `-0.168` n `20`; unknown avg `-0.3864` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
