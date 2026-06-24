# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T19:22:28.299306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6597` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3929` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9376` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0536` n `12`; crypto_alt avg `-0.2152` n `228`; crypto_major avg `-0.2534` n `8`; equity avg `0.0291` n `86`; fx avg `-0.0087` n `6`; index avg `-0.0079` n `23`; metal avg `0.0028` n `20`; unknown avg `-0.228` n `764`
- 1h: commodity avg `-0.0644` n `12`; crypto_alt avg `-0.4626` n `228`; crypto_major avg `-0.5952` n `8`; equity avg `-0.7497` n `86`; fx avg `0.0081` n `6`; index avg `-0.1007` n `23`; metal avg `-0.0658` n `20`; unknown avg `-0.3431` n `764`
- 4h: commodity avg `0.0156` n `12`; crypto_alt avg `-2.9325` n `228`; crypto_major avg `-2.6441` n `8`; equity avg `-1.8126` n `86`; fx avg `0.0124` n `6`; index avg `-0.2512` n `23`; metal avg `-0.7065` n `20`; unknown avg `-0.8318` n `764`
- 24h: commodity avg `-0.5423` n `12`; crypto_alt avg `-4.1365` n `228`; crypto_major avg `-3.8345` n `8`; equity avg `1.6835` n `86`; fx avg `0.0641` n `6`; index avg `-0.0505` n `23`; metal avg `-2.0358` n `20`; unknown avg `-0.3145` n `724`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
