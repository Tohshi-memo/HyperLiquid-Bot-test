# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T23:57:39.448873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2578` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `-0.2251` n `231`; crypto_major avg `-0.2547` n `8`; equity avg `-0.1408` n `122`; fx avg `-0.0015` n `6`; index avg `-0.0505` n `25`; metal avg `-0.0233` n `20`; unknown avg `-0.0271` n `796`
- 1h: commodity avg `0.0245` n `12`; crypto_alt avg `-0.5776` n `231`; crypto_major avg `-0.5996` n `8`; equity avg `-0.291` n `122`; fx avg `-0.0087` n `6`; index avg `-0.0732` n `25`; metal avg `-0.0902` n `20`; unknown avg `-0.1207` n `795`
- 4h: commodity avg `-0.0946` n `12`; crypto_alt avg `-1.2196` n `231`; crypto_major avg `-1.305` n `8`; equity avg `-0.165` n `122`; fx avg `0.0023` n `6`; index avg `-0.0472` n `25`; metal avg `-0.0697` n `20`; unknown avg `-0.4526` n `795`
- 24h: commodity avg `-0.7133` n `12`; crypto_alt avg `-2.2226` n `231`; crypto_major avg `-1.4543` n `8`; equity avg `1.9825` n `122`; fx avg `0.0464` n `6`; index avg `0.2089` n `25`; metal avg `-0.2496` n `20`; unknown avg `-0.4776` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
