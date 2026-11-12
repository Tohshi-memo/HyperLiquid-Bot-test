# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T15:37:33.160321+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5088` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.079` n `13`; crypto_alt avg `-0.064` n `239`; crypto_major avg `-0.0358` n `8`; equity avg `0.0437` n `162`; fx avg `-0.0057` n `6`; index avg `0.0039` n `27`; metal avg `0.0375` n `20`; unknown avg `0.3234` n `1261`
- 1h: commodity avg `0.0164` n `13`; crypto_alt avg `-0.8939` n `239`; crypto_major avg `-0.7115` n `8`; equity avg `-0.1266` n `162`; fx avg `-0.0337` n `6`; index avg `-0.0067` n `27`; metal avg `-0.2719` n `20`; unknown avg `0.8434` n `1253`
- 4h: commodity avg `0.1704` n `13`; crypto_alt avg `-1.3829` n `239`; crypto_major avg `-1.5047` n `8`; equity avg `-0.9734` n `162`; fx avg `-0.048` n `6`; index avg `0.0041` n `27`; metal avg `-0.51` n `20`; unknown avg `19.7205` n `1239`
- 24h: commodity avg `-0.3874` n `13`; crypto_alt avg `-4.6468` n `239`; crypto_major avg `-4.1275` n `8`; equity avg `-3.1244` n `162`; fx avg `-0.133` n `6`; index avg `-0.128` n `27`; metal avg `-1.1381` n `20`; unknown avg `4.9419` n `1148`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
