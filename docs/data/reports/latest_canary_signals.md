# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T03:22:25.427342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1198` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0213` n `12`; crypto_alt avg `0.4196` n `231`; crypto_major avg `0.4268` n `8`; equity avg `0.0624` n `127`; fx avg `-0.0044` n `6`; index avg `0.0056` n `26`; metal avg `0.0168` n `20`; unknown avg `-0.0646` n `792`
- 1h: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.4239` n `231`; crypto_major avg `-0.0527` n `8`; equity avg `-0.0787` n `127`; fx avg `-0.0055` n `6`; index avg `-0.0069` n `26`; metal avg `0.0646` n `20`; unknown avg `-0.0431` n `792`
- 4h: commodity avg `-0.0342` n `12`; crypto_alt avg `-1.2995` n `231`; crypto_major avg `-1.0506` n `8`; equity avg `0.2047` n `127`; fx avg `-0.0517` n `6`; index avg `0.0692` n `26`; metal avg `-0.068` n `20`; unknown avg `0.0218` n `792`
- 24h: commodity avg `0.3032` n `12`; crypto_alt avg `0.3093` n `231`; crypto_major avg `1.7068` n `8`; equity avg `-0.1116` n `127`; fx avg `-0.0345` n `6`; index avg `0.0365` n `26`; metal avg `-0.153` n `20`; unknown avg `0.4652` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
