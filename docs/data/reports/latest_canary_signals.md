# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T10:01:57.554892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0237` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0402` n `12`; crypto_alt avg `-0.092` n `231`; crypto_major avg `-0.0888` n `8`; equity avg `-0.0104` n `122`; fx avg `-0.0033` n `6`; index avg `0.0007` n `25`; metal avg `-0.0133` n `20`; unknown avg `-0.0267` n `797`
- 1h: commodity avg `0.0748` n `12`; crypto_alt avg `-0.7744` n `231`; crypto_major avg `-0.6623` n `8`; equity avg `0.0247` n `122`; fx avg `0.0009` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0262` n `20`; unknown avg `-0.154` n `797`
- 4h: commodity avg `-0.1175` n `12`; crypto_alt avg `-1.0564` n `231`; crypto_major avg `-1.0409` n `8`; equity avg `-0.0359` n `122`; fx avg `-0.0124` n `6`; index avg `-0.0172` n `25`; metal avg `-0.1481` n `20`; unknown avg `-0.0501` n `797`
- 24h: commodity avg `-0.3159` n `12`; crypto_alt avg `-2.212` n `231`; crypto_major avg `-1.9609` n `8`; equity avg `0.0038` n `122`; fx avg `-0.0364` n `6`; index avg `-0.0633` n `25`; metal avg `0.1412` n `20`; unknown avg `0.6201` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
