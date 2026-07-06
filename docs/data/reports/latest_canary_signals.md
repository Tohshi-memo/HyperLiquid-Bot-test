# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T06:22:25.770760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2608` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `-0.0171` n `229`; crypto_major avg `-0.0229` n `8`; equity avg `-0.094` n `88`; fx avg `0.0264` n `6`; index avg `-0.0018` n `25`; metal avg `0.0286` n `20`; unknown avg `-0.0393` n `765`
- 1h: commodity avg `0.1875` n `12`; crypto_alt avg `-0.2527` n `229`; crypto_major avg `-0.2739` n `8`; equity avg `-0.0509` n `88`; fx avg `0.0281` n `6`; index avg `0.0091` n `25`; metal avg `0.034` n `20`; unknown avg `-0.0984` n `733`
- 4h: commodity avg `0.1316` n `12`; crypto_alt avg `-1.2694` n `229`; crypto_major avg `-1.2073` n `8`; equity avg `0.046` n `88`; fx avg `-0.0017` n `6`; index avg `0.0535` n `25`; metal avg `-0.2643` n `20`; unknown avg `-0.2583` n `733`
- 24h: commodity avg `0.0189` n `12`; crypto_alt avg `0.0447` n `229`; crypto_major avg `0.8838` n `8`; equity avg `-0.7656` n `88`; fx avg `0.0939` n `6`; index avg `-0.0734` n `25`; metal avg `-0.2707` n `20`; unknown avg `0.991` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
