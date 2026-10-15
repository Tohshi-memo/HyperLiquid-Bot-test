# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T13:37:34.418398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1632` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0077` n `13`; crypto_alt avg `0.0304` n `236`; crypto_major avg `0.0238` n `8`; equity avg `-0.4361` n `151`; fx avg `0.0049` n `6`; index avg `-0.0066` n `26`; metal avg `0.0506` n `20`; unknown avg `-0.1103` n `1136`
- 1h: commodity avg `0.1518` n `13`; crypto_alt avg `-0.2987` n `236`; crypto_major avg `-0.4815` n `8`; equity avg `-0.5596` n `151`; fx avg `-0.0284` n `6`; index avg `-0.0111` n `26`; metal avg `0.0518` n `20`; unknown avg `-0.2761` n `1134`
- 4h: commodity avg `0.004` n `13`; crypto_alt avg `-1.005` n `236`; crypto_major avg `-1.2096` n `8`; equity avg `-1.0424` n `151`; fx avg `-0.0322` n `6`; index avg `-0.0464` n `26`; metal avg `0.0223` n `20`; unknown avg `0.579` n `1048`
- 24h: commodity avg `-0.2602` n `13`; crypto_alt avg `-4.4074` n `236`; crypto_major avg `-3.6574` n `8`; equity avg `-5.2708` n `151`; fx avg `0.1334` n `6`; index avg `-0.7887` n `26`; metal avg `0.014` n `20`; unknown avg `-0.3332` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1207`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0955`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0911`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0812`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0743`, n `666`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0715`, n `666`, weak_sample_signal
