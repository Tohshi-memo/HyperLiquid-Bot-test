# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T02:37:31.735898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2206` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.0449` n `230`; crypto_major avg `-0.1463` n `8`; equity avg `-0.3096` n `102`; fx avg `-0.0253` n `6`; index avg `-0.0776` n `25`; metal avg `-0.0336` n `20`; unknown avg `-0.0315` n `774`
- 1h: commodity avg `-0.119` n `12`; crypto_alt avg `0.2334` n `230`; crypto_major avg `-0.0333` n `8`; equity avg `-0.6459` n `102`; fx avg `-0.0672` n `6`; index avg `-0.1065` n `25`; metal avg `-0.0547` n `20`; unknown avg `-0.1569` n `774`
- 4h: commodity avg `-0.1602` n `12`; crypto_alt avg `-1.6072` n `230`; crypto_major avg `-1.5593` n `8`; equity avg `-1.6958` n `102`; fx avg `0.003` n `6`; index avg `-0.3387` n `25`; metal avg `-0.3147` n `20`; unknown avg `0.3921` n `774`
- 24h: commodity avg `-0.9295` n `12`; crypto_alt avg `-3.917` n `230`; crypto_major avg `-3.3173` n `8`; equity avg `-3.2356` n `102`; fx avg `-0.1363` n `6`; index avg `-0.716` n `25`; metal avg `-0.3506` n `20`; unknown avg `1161.8427` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
