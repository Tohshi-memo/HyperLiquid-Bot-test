# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T22:52:27.247721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.2649` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.2548` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.0124` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0284` n `13`; crypto_alt avg `-0.4814` n `238`; crypto_major avg `-0.4783` n `8`; equity avg `-0.2825` n `156`; fx avg `0.0051` n `6`; index avg `-0.0305` n `27`; metal avg `-0.0149` n `20`; unknown avg `4.199` n `1260`
- 1h: commodity avg `0.0026` n `13`; crypto_alt avg `-0.3118` n `238`; crypto_major avg `-0.3226` n `8`; equity avg `-0.4116` n `156`; fx avg `0.0328` n `6`; index avg `-0.0649` n `27`; metal avg `0.0027` n `20`; unknown avg `0.0905` n `1252`
- 4h: commodity avg `0.0406` n `13`; crypto_alt avg `-4.6668` n `238`; crypto_major avg `-3.2243` n `8`; equity avg `-2.5827` n `156`; fx avg `0.0383` n `6`; index avg `-0.2119` n `27`; metal avg `0.0305` n `20`; unknown avg `24.1184` n `1162`
- 24h: commodity avg `-0.2451` n `13`; crypto_alt avg `-5.7152` n `238`; crypto_major avg `-2.16` n `8`; equity avg `-3.458` n `155`; fx avg `0.0813` n `6`; index avg `-0.276` n `27`; metal avg `-0.554` n `20`; unknown avg `30.4867` n `994`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
