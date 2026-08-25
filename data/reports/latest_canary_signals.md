# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T23:22:31.289339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6697` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5228` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0116` n `12`; crypto_alt avg `-0.315` n `231`; crypto_major avg `-0.2685` n `8`; equity avg `-0.0705` n `122`; fx avg `0.0009` n `6`; index avg `-0.0121` n `25`; metal avg `-0.0415` n `20`; unknown avg `-0.1413` n `795`
- 1h: commodity avg `0.0056` n `12`; crypto_alt avg `-0.2291` n `231`; crypto_major avg `-0.1888` n `8`; equity avg `-0.0404` n `122`; fx avg `0.0049` n `6`; index avg `-0.0151` n `25`; metal avg `-0.0166` n `20`; unknown avg `-0.1375` n `795`
- 4h: commodity avg `-0.2319` n `12`; crypto_alt avg `-1.338` n `231`; crypto_major avg `-1.4833` n `8`; equity avg `0.1864` n `122`; fx avg `0.0019` n `6`; index avg `0.0395` n `25`; metal avg `-0.022` n `20`; unknown avg `-0.0906` n `795`
- 24h: commodity avg `-0.7157` n `12`; crypto_alt avg `-1.7474` n `231`; crypto_major avg `-0.9652` n `8`; equity avg `2.0787` n `122`; fx avg `0.056` n `6`; index avg `0.2422` n `25`; metal avg `-0.1632` n `20`; unknown avg `-0.4703` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
