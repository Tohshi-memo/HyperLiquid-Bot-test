# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T08:30:24.740830+00:00`
- Correlation status: `ready`
- Asset price records: `249`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0365` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1718` n `7`; crypto_alt avg `-0.1376` n `223`; crypto_major avg `-0.1454` n `7`; equity avg `-0.0509` n `42`; fx avg `0.0019` n `4`; index avg `0.041` n `9`; metal avg `-0.0424` n `7`; unknown avg `-0.1287` n `314`
- 1h: commodity avg `0.2104` n `7`; crypto_alt avg `-0.0916` n `223`; crypto_major avg `-0.2139` n `7`; equity avg `-0.2334` n `42`; fx avg `-0.0109` n `4`; index avg `-0.085` n `9`; metal avg `-0.5201` n `7`; unknown avg `0.2987` n `314`
- 4h: commodity avg `0.5576` n `7`; crypto_alt avg `-0.4751` n `223`; crypto_major avg `-1.0669` n `7`; equity avg `-0.3777` n `42`; fx avg `0.0135` n `4`; index avg `-0.0304` n `9`; metal avg `-1.2393` n `7`; unknown avg `-0.2491` n `312`
- 24h: commodity avg `0.6636` n `7`; crypto_alt avg `1.902` n `223`; crypto_major avg `1.9979` n `7`; equity avg `0.9082` n `42`; fx avg `-0.0621` n `4`; index avg `0.7754` n `9`; metal avg `-0.9924` n `7`; unknown avg `0.2313` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3362`, n `245`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3314`, n `241`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3254`, n `241`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3252`, n `245`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2115`, n `241`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2006`, n `241`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1918`, n `245`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1778`, n `245`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1728`, n `241`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1718`, n `245`, weak_sample_signal
