# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T02:52:28.515579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5752` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3773` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1965` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0844` n `13`; crypto_alt avg `-0.6831` n `239`; crypto_major avg `-0.6809` n `8`; equity avg `-0.4177` n `162`; fx avg `-0.017` n `6`; index avg `-0.0466` n `27`; metal avg `-0.043` n `20`; unknown avg `1.9869` n `1260`
- 1h: commodity avg `0.0337` n `13`; crypto_alt avg `-1.246` n `239`; crypto_major avg `-1.266` n `8`; equity avg `-0.7717` n `162`; fx avg `0.0014` n `6`; index avg `-0.0695` n `27`; metal avg `-0.0553` n `20`; unknown avg `2.0044` n `1258`
- 4h: commodity avg `-0.1111` n `13`; crypto_alt avg `-1.208` n `239`; crypto_major avg `-1.3115` n `8`; equity avg `-0.0588` n `162`; fx avg `-0.0144` n `6`; index avg `0.0658` n `27`; metal avg `0.2637` n `20`; unknown avg `164.0128` n `1249`
- 24h: commodity avg `0.771` n `13`; crypto_alt avg `-2.0795` n `239`; crypto_major avg `-3.2704` n `8`; equity avg `-1.1909` n `162`; fx avg `-0.0496` n `6`; index avg `0.0233` n `27`; metal avg `-0.4124` n `20`; unknown avg `51.1275` n `1119`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
