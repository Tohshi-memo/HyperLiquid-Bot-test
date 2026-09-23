# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T10:37:28.161325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2328` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0482` n `12`; crypto_alt avg `0.2014` n `234`; crypto_major avg `0.1783` n `8`; equity avg `0.0139` n `140`; fx avg `-0.0039` n `6`; index avg `-0.0069` n `26`; metal avg `0.0036` n `20`; unknown avg `0.3625` n `946`
- 1h: commodity avg `-0.0391` n `12`; crypto_alt avg `-0.1831` n `234`; crypto_major avg `-0.0987` n `8`; equity avg `-0.0441` n `140`; fx avg `0.001` n `6`; index avg `-0.0118` n `26`; metal avg `-0.0137` n `20`; unknown avg `0.7708` n `943`
- 4h: commodity avg `0.1832` n `12`; crypto_alt avg `-0.7311` n `234`; crypto_major avg `-1.3027` n `8`; equity avg `-0.2316` n `140`; fx avg `0.0335` n `6`; index avg `-0.0699` n `26`; metal avg `-0.2197` n `20`; unknown avg `1.0692` n `937`
- 24h: commodity avg `0.6981` n `12`; crypto_alt avg `3.8287` n `234`; crypto_major avg `0.8072` n `8`; equity avg `0.8044` n `140`; fx avg `0.0045` n `6`; index avg `0.0635` n `26`; metal avg `-0.1454` n `20`; unknown avg `1.4491` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
