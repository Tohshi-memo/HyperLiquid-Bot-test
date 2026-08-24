# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T01:54:18.519107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5876` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5533` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0208` n `12`; crypto_alt avg `-0.2041` n `231`; crypto_major avg `-0.1189` n `8`; equity avg `-0.1721` n `122`; fx avg `-0.016` n `6`; index avg `-0.0154` n `25`; metal avg `0.042` n `20`; unknown avg `-0.0562` n `793`
- 1h: commodity avg `-0.0888` n `12`; crypto_alt avg `-1.0308` n `231`; crypto_major avg `-0.9104` n `8`; equity avg `-0.4812` n `122`; fx avg `0.0161` n `6`; index avg `-0.0343` n `25`; metal avg `-0.0251` n `20`; unknown avg `0.9112` n `793`
- 4h: commodity avg `-0.2622` n `12`; crypto_alt avg `-2.4501` n `231`; crypto_major avg `-1.6357` n `8`; equity avg `-0.8528` n `122`; fx avg `-0.0283` n `6`; index avg `-0.0824` n `25`; metal avg `-0.0481` n `20`; unknown avg `0.9225` n `793`
- 24h: commodity avg `-0.3865` n `12`; crypto_alt avg `1.6923` n `231`; crypto_major avg `-0.4375` n `8`; equity avg `-0.2748` n `122`; fx avg `-0.1545` n `6`; index avg `0.0182` n `25`; metal avg `0.0352` n `20`; unknown avg `6.1213` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
