# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T02:37:31.772393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4435` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0382` n `12`; crypto_alt avg `0.5608` n `228`; crypto_major avg `0.3884` n `8`; equity avg `-0.1487` n `86`; fx avg `-0.0124` n `6`; index avg `-0.0535` n `23`; metal avg `-0.2097` n `20`; unknown avg `22.0847` n `765`
- 1h: commodity avg `-0.0932` n `12`; crypto_alt avg `-1.1515` n `228`; crypto_major avg `-1.0439` n `8`; equity avg `-1.0294` n `86`; fx avg `-0.0252` n `6`; index avg `-0.2171` n `23`; metal avg `-0.4395` n `20`; unknown avg `4.1321` n `765`
- 4h: commodity avg `-0.0613` n `12`; crypto_alt avg `-1.7571` n `228`; crypto_major avg `-1.8014` n `8`; equity avg `-1.6394` n `86`; fx avg `0.0201` n `6`; index avg `-0.3579` n `23`; metal avg `-0.6793` n `20`; unknown avg `-0.9045` n `749`
- 24h: commodity avg `0.3849` n `12`; crypto_alt avg `-2.9986` n `228`; crypto_major avg `-3.1612` n `8`; equity avg `-3.7433` n `86`; fx avg `0.0231` n `6`; index avg `-0.537` n `23`; metal avg `-0.1176` n `20`; unknown avg `0.249` n `716`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
