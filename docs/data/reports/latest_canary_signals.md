# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T21:52:20.026796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6962` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4967` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `-0.0835` n `231`; crypto_major avg `-0.0146` n `8`; equity avg `0.0691` n `122`; fx avg `0.0034` n `6`; index avg `0.0049` n `25`; metal avg `0.0167` n `20`; unknown avg `0.0242` n `795`
- 1h: commodity avg `0.0109` n `12`; crypto_alt avg `-0.0561` n `231`; crypto_major avg `0.0304` n `8`; equity avg `0.0987` n `122`; fx avg `0.0085` n `6`; index avg `-0.0041` n `25`; metal avg `-0.0225` n `20`; unknown avg `0.147` n `795`
- 4h: commodity avg `-0.1488` n `12`; crypto_alt avg `-1.6419` n `231`; crypto_major avg `-1.4316` n `8`; equity avg `0.2646` n `122`; fx avg `-0.0026` n `6`; index avg `0.0651` n `25`; metal avg `0.0536` n `20`; unknown avg `-0.3084` n `795`
- 24h: commodity avg `-0.6993` n `12`; crypto_alt avg `-2.475` n `231`; crypto_major avg `-1.0994` n `8`; equity avg `2.0161` n `122`; fx avg `0.0513` n `6`; index avg `0.2592` n `25`; metal avg `-0.0672` n `20`; unknown avg `-0.6328` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
