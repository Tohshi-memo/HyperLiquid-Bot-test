# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T03:22:30.957202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0071` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `-0.1226` n `232`; crypto_major avg `-0.1512` n `8`; equity avg `0.0945` n `134`; fx avg `0.0096` n `6`; index avg `0.0289` n `26`; metal avg `0.0801` n `20`; unknown avg `0.9765` n `797`
- 1h: commodity avg `0.0531` n `12`; crypto_alt avg `-1.1381` n `232`; crypto_major avg `-0.991` n `8`; equity avg `-0.0742` n `134`; fx avg `0.0351` n `6`; index avg `0.0161` n `26`; metal avg `0.0355` n `20`; unknown avg `0.6307` n `795`
- 4h: commodity avg `-0.0588` n `12`; crypto_alt avg `0.0889` n `232`; crypto_major avg `-0.5035` n `8`; equity avg `0.6076` n `134`; fx avg `-0.1374` n `6`; index avg `0.171` n `26`; metal avg `0.1659` n `20`; unknown avg `1.1018` n `783`
- 24h: commodity avg `0.1649` n `12`; crypto_alt avg `0.1583` n `232`; crypto_major avg `-1.3625` n `8`; equity avg `0.6683` n `134`; fx avg `-0.3307` n `6`; index avg `0.2198` n `26`; metal avg `0.3207` n `20`; unknown avg `7374.0849` n `678`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
