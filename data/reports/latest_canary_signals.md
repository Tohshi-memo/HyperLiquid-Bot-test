# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T22:59:24.115897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0864` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `0.0724` n `231`; crypto_major avg `0.0499` n `8`; equity avg `0.0374` n `122`; fx avg `-0.0014` n `6`; index avg `-0.0041` n `25`; metal avg `0.0096` n `20`; unknown avg `0.0586` n `795`
- 1h: commodity avg `-0.0164` n `12`; crypto_alt avg `0.6056` n `231`; crypto_major avg `0.4462` n `8`; equity avg `0.0768` n `122`; fx avg `0.001` n `6`; index avg `-0.0024` n `25`; metal avg `0.0933` n `20`; unknown avg `0.0997` n `795`
- 4h: commodity avg `-0.2334` n `12`; crypto_alt avg `-1.1485` n `231`; crypto_major avg `-1.0646` n `8`; equity avg `0.1208` n `122`; fx avg `-0.0076` n `6`; index avg `0.0218` n `25`; metal avg `0.1322` n `20`; unknown avg `-0.3318` n `795`
- 24h: commodity avg `-0.7132` n `12`; crypto_alt avg `-1.6537` n `231`; crypto_major avg `-0.5665` n `8`; equity avg `2.1664` n `122`; fx avg `0.059` n `6`; index avg `0.2546` n `25`; metal avg `-0.0466` n `20`; unknown avg `-0.4784` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
