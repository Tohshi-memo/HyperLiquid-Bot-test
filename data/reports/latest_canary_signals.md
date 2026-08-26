# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T00:07:43.479673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0785` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.037` n `12`; crypto_alt avg `-0.0251` n `231`; crypto_major avg `-0.0881` n `8`; equity avg `-0.1133` n `122`; fx avg `0.0285` n `6`; index avg `-0.0391` n `25`; metal avg `0.0099` n `20`; unknown avg `0.0163` n `796`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.6532` n `231`; crypto_major avg `-0.6908` n `8`; equity avg `-0.3895` n `122`; fx avg `0.0171` n `6`; index avg `-0.11` n `25`; metal avg `-0.0648` n `20`; unknown avg `-0.2547` n `795`
- 4h: commodity avg `0.04` n `12`; crypto_alt avg `-1.0019` n `231`; crypto_major avg `-1.1927` n `8`; equity avg `-0.3398` n `122`; fx avg `0.0201` n `6`; index avg `-0.1142` n `25`; metal avg `-0.0444` n `20`; unknown avg `-0.3946` n `795`
- 24h: commodity avg `-0.7485` n `12`; crypto_alt avg `-2.5345` n `231`; crypto_major avg `-1.8517` n `8`; equity avg `2.001` n `122`; fx avg `0.0856` n `6`; index avg `0.2272` n `25`; metal avg `-0.2396` n `20`; unknown avg `-0.5479` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
