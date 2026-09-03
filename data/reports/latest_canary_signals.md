# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T13:37:38.066662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.3225` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0146` n `12`; crypto_alt avg `-0.1554` n `232`; crypto_major avg `0.0131` n `8`; equity avg `-0.4314` n `133`; fx avg `0.0027` n `6`; index avg `-0.0255` n `26`; metal avg `-0.0444` n `20`; unknown avg `1.5538` n `792`
- 1h: commodity avg `-0.1483` n `12`; crypto_alt avg `-0.2325` n `232`; crypto_major avg `0.2212` n `8`; equity avg `-0.2549` n `133`; fx avg `0.0179` n `6`; index avg `0.0117` n `26`; metal avg `0.024` n `20`; unknown avg `1.763` n `790`
- 4h: commodity avg `0.0009` n `12`; crypto_alt avg `0.2233` n `232`; crypto_major avg `1.0873` n `8`; equity avg `-0.0173` n `133`; fx avg `-0.0607` n `6`; index avg `3.4098` n `26`; metal avg `0.2326` n `20`; unknown avg `4.0392` n `790`
- 24h: commodity avg `0.5039` n `12`; crypto_alt avg `2.4206` n `232`; crypto_major avg `2.8527` n `8`; equity avg `1.037` n `133`; fx avg `-0.3197` n `6`; index avg `0.0972` n `26`; metal avg `0.5433` n `20`; unknown avg `0.1376` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0406`, n `668`, weak_sample_signal
