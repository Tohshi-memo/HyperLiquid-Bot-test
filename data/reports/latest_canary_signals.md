# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T13:07:27.739359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.02` - Polymarket crypto volume is unusually high.
- 1h_commodity_crypto_divergence: score `-2.2602` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `-2.1576` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.1056` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `2.0971` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.8089` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `-1.7828` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0353` n `12`; crypto_alt avg `-0.2426` n `232`; crypto_major avg `-0.2848` n `8`; equity avg `-0.0183` n `133`; fx avg `0.0714` n `6`; index avg `-0.0075` n `26`; metal avg `-0.0637` n `20`; unknown avg `2.4609` n `777`
- 1h: commodity avg `0.048` n `12`; crypto_alt avg `-2.1125` n `232`; crypto_major avg `-2.2122` n `8`; equity avg `-0.7959` n `133`; fx avg `-0.0997` n `6`; index avg `-0.1151` n `26`; metal avg `-0.4033` n `20`; unknown avg `1.6905` n `771`
- 4h: commodity avg `-0.0637` n `12`; crypto_alt avg `-2.0828` n `232`; crypto_major avg `-2.2213` n `8`; equity avg `-0.8021` n `133`; fx avg `-0.1421` n `6`; index avg `-0.1157` n `26`; metal avg `-0.4385` n `20`; unknown avg `1.0199` n `771`
- 24h: commodity avg `-0.4017` n `12`; crypto_alt avg `0.1517` n `232`; crypto_major avg `1.0609` n `8`; equity avg `0.8898` n `133`; fx avg `-0.0799` n `6`; index avg `0.1798` n `26`; metal avg `-0.2658` n `20`; unknown avg `1.0357` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
