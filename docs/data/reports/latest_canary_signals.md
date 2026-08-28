# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T03:37:25.355972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1453` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `-0.1168` n `231`; crypto_major avg `-0.0968` n `8`; equity avg `-0.0477` n `127`; fx avg `-0.0047` n `6`; index avg `-0.0112` n `26`; metal avg `-0.0262` n `20`; unknown avg `0.143` n `792`
- 1h: commodity avg `0.0086` n `12`; crypto_alt avg `-0.185` n `231`; crypto_major avg `-0.2167` n `8`; equity avg `-0.0103` n `127`; fx avg `-0.0294` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0016` n `20`; unknown avg `0.132` n `792`
- 4h: commodity avg `-0.0087` n `12`; crypto_alt avg `-1.3351` n `231`; crypto_major avg `-1.08` n `8`; equity avg `0.1575` n `127`; fx avg `-0.0555` n `6`; index avg `0.0653` n `26`; metal avg `-0.0914` n `20`; unknown avg `0.1555` n `792`
- 24h: commodity avg `0.2895` n `12`; crypto_alt avg `0.1958` n `231`; crypto_major avg `1.6335` n `8`; equity avg `-0.1032` n `127`; fx avg `-0.0297` n `6`; index avg `0.0238` n `26`; metal avg `-0.1493` n `20`; unknown avg `0.6325` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
