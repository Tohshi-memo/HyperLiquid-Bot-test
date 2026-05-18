# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T00:37:16.971986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1597` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.0237` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0143` n `12`; crypto_alt avg `-0.0957` n `228`; crypto_major avg `-0.0866` n `8`; equity avg `-0.1184` n `66`; fx avg `0.0126` n `5`; index avg `-0.0022` n `23`; metal avg `-0.8041` n `18`; unknown avg `-0.1517` n `383`
- 1h: commodity avg `0.2585` n `12`; crypto_alt avg `-1.1505` n `228`; crypto_major avg `-0.7775` n `8`; equity avg `-0.7727` n `66`; fx avg `0.0411` n `5`; index avg `-0.3738` n `23`; metal avg `-1.2473` n `18`; unknown avg `0.7895` n `383`
- 4h: commodity avg `0.5729` n `12`; crypto_alt avg `-2.3018` n `228`; crypto_major avg `-1.5868` n `8`; equity avg `-0.8196` n `66`; fx avg `0.0154` n `5`; index avg `-0.5631` n `23`; metal avg `-0.7625` n `18`; unknown avg `1.2878` n `383`
- 24h: commodity avg `2.3112` n `12`; crypto_alt avg `-11.193` n `228`; crypto_major avg `-3.0024` n `8`; equity avg `-3.7373` n `65`; fx avg `-0.136` n `5`; index avg `-2.0366` n `23`; metal avg `-6.6453` n `18`; unknown avg `549.9909` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
