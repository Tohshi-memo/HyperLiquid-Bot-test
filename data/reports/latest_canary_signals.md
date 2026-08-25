# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T21:37:35.263561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.554` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4374` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.023` n `12`; crypto_alt avg `0.5833` n `231`; crypto_major avg `0.5522` n `8`; equity avg `0.0526` n `122`; fx avg `0.01` n `6`; index avg `-0.0072` n `25`; metal avg `0.0213` n `20`; unknown avg `0.2514` n `795`
- 1h: commodity avg `0.0739` n `12`; crypto_alt avg `-0.6271` n `231`; crypto_major avg `-0.5739` n `8`; equity avg `-0.1029` n `122`; fx avg `-0.0101` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0614` n `20`; unknown avg `-0.1177` n `795`
- 4h: commodity avg `-0.1819` n `12`; crypto_alt avg `-1.5299` n `231`; crypto_major avg `-1.3776` n `8`; equity avg `0.1764` n `122`; fx avg `-0.0073` n `6`; index avg `0.0598` n `25`; metal avg `0.0472` n `20`; unknown avg `-0.3589` n `795`
- 24h: commodity avg `-0.7065` n `12`; crypto_alt avg `-2.4893` n `231`; crypto_major avg `-1.0351` n `8`; equity avg `1.9409` n `122`; fx avg `0.054` n `6`; index avg `0.2551` n `25`; metal avg `-0.0703` n `20`; unknown avg `-0.6208` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
