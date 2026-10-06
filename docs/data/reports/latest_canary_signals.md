# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T19:22:33.927483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1573` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.014` n `13`; crypto_alt avg `-0.3231` n `235`; crypto_major avg `-0.2152` n `8`; equity avg `-0.0796` n `150`; fx avg `0.01` n `6`; index avg `-0.0116` n `26`; metal avg `-0.0343` n `20`; unknown avg `1.1842` n `1076`
- 1h: commodity avg `0.246` n `13`; crypto_alt avg `-0.4555` n `235`; crypto_major avg `-0.4228` n `8`; equity avg `-0.1777` n `150`; fx avg `0.0026` n `6`; index avg `-0.0322` n `26`; metal avg `0.0389` n `20`; unknown avg `3.2376` n `1074`
- 4h: commodity avg `0.6013` n `13`; crypto_alt avg `-1.207` n `235`; crypto_major avg `-1.2781` n `8`; equity avg `-0.51` n `150`; fx avg `0.0004` n `6`; index avg `-0.1208` n `26`; metal avg `0.1176` n `20`; unknown avg `3.5568` n `1068`
- 24h: commodity avg `0.2885` n `13`; crypto_alt avg `-0.7278` n `235`; crypto_major avg `-0.5673` n `8`; equity avg `0.4877` n `149`; fx avg `0.1104` n `6`; index avg `-0.0115` n `26`; metal avg `0.0647` n `20`; unknown avg `382.7938` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
