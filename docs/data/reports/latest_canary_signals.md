# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T15:37:33.076554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1568` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0384` n `12`; crypto_alt avg `-0.8699` n `232`; crypto_major avg `-0.687` n `8`; equity avg `-0.0626` n `134`; fx avg `0.0026` n `6`; index avg `0.0128` n `26`; metal avg `-0.0148` n `20`; unknown avg `-0.5443` n `796`
- 1h: commodity avg `0.0311` n `12`; crypto_alt avg `-0.9572` n `232`; crypto_major avg `-0.6881` n `8`; equity avg `-0.0738` n `134`; fx avg `0.0038` n `6`; index avg `-0.0004` n `26`; metal avg `0.0357` n `20`; unknown avg `-0.495` n `794`
- 4h: commodity avg `0.0192` n `12`; crypto_alt avg `-0.7774` n `232`; crypto_major avg `-1.1237` n `8`; equity avg `-0.064` n `134`; fx avg `-0.044` n `6`; index avg `0.0331` n `26`; metal avg `0.2039` n `20`; unknown avg `6683.8312` n `748`
- 24h: commodity avg `0.2439` n `12`; crypto_alt avg `0.0789` n `232`; crypto_major avg `-1.3043` n `8`; equity avg `0.383` n `134`; fx avg `-0.1114` n `6`; index avg `0.0425` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.0743` n `680`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
