# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T00:09:42.910726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.2674` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.7237` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6503` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.3724` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1687` n `12`; crypto_alt avg `-0.5477` n `230`; crypto_major avg `-0.5551` n `8`; equity avg `-0.0637` n `92`; fx avg `0.0006` n `6`; index avg `0.0085` n `25`; metal avg `-0.007` n `20`; unknown avg `0.0131` n `765`
- 1h: commodity avg `0.3176` n `12`; crypto_alt avg `-1.563` n `230`; crypto_major avg `-1.4261` n `8`; equity avg `-0.1643` n `92`; fx avg `0.0113` n `6`; index avg `-0.0537` n `25`; metal avg `-0.0176` n `20`; unknown avg `0.7796` n `765`
- 4h: commodity avg `0.5179` n `12`; crypto_alt avg `-2.1503` n `230`; crypto_major avg `-1.7495` n `8`; equity avg `-0.2626` n `92`; fx avg `0.017` n `6`; index avg `-0.0992` n `25`; metal avg `-0.0258` n `20`; unknown avg `1.0063` n `765`
- 24h: commodity avg `0.5179` n `12`; crypto_alt avg `-1.2882` n `229`; crypto_major avg `-1.0258` n `8`; equity avg `0.0014` n `92`; fx avg `0.0185` n `6`; index avg `-0.058` n `25`; metal avg `-0.054` n `20`; unknown avg `1.9544` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
