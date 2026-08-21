# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T12:52:23.910490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3674` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0686` n `12`; crypto_alt avg `0.2811` n `230`; crypto_major avg `0.3543` n `8`; equity avg `0.0914` n `121`; fx avg `-0.0188` n `6`; index avg `0.0024` n `25`; metal avg `0.0745` n `20`; unknown avg `0.0546` n `793`
- 1h: commodity avg `0.0739` n `12`; crypto_alt avg `0.9485` n `230`; crypto_major avg `0.6464` n `8`; equity avg `0.095` n `121`; fx avg `0.0089` n `6`; index avg `0.0008` n `23`; metal avg `-0.0646` n `18`; unknown avg `0.0154` n `774`
- 4h: commodity avg `0.1782` n `12`; crypto_alt avg `0.7122` n `230`; crypto_major avg `-1.3423` n `8`; equity avg `0.1159` n `121`; fx avg `0.0189` n `6`; index avg `0.0251` n `25`; metal avg `-0.0615` n `20`; unknown avg `0.41` n `793`
- 24h: commodity avg `0.178` n `12`; crypto_alt avg `8.24` n `230`; crypto_major avg `6.4771` n `8`; equity avg `1.6784` n `121`; fx avg `-0.0927` n `6`; index avg `0.2261` n `25`; metal avg `0.9127` n `20`; unknown avg `2.385` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2332`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
