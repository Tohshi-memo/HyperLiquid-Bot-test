# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T17:07:30.647475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.381` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.1524` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.0299` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0592` n `13`; crypto_alt avg `-0.5131` n `235`; crypto_major avg `-0.4228` n `8`; equity avg `-0.3348` n `150`; fx avg `-0.0156` n `6`; index avg `-0.0726` n `26`; metal avg `0.0932` n `20`; unknown avg `2.0399` n `1075`
- 1h: commodity avg `-0.3781` n `13`; crypto_alt avg `-0.3206` n `235`; crypto_major avg `-0.4944` n `8`; equity avg `-1.13` n `150`; fx avg `-0.035` n `6`; index avg `-0.1588` n `26`; metal avg `0.1937` n `20`; unknown avg `1.5804` n `1075`
- 4h: commodity avg `-0.3742` n `13`; crypto_alt avg `-4.2232` n `235`; crypto_major avg `-3.4041` n `8`; equity avg `-1.9859` n `150`; fx avg `-0.0226` n `6`; index avg `-0.2517` n `26`; metal avg `-0.0231` n `20`; unknown avg `0.8517` n `1021`
- 24h: commodity avg `0.6528` n `13`; crypto_alt avg `-4.3705` n `235`; crypto_major avg `-5.3502` n `8`; equity avg `-3.2835` n `150`; fx avg `0.0535` n `6`; index avg `-0.4581` n `26`; metal avg `-0.1314` n `20`; unknown avg `23.3284` n `991`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
