# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T14:37:14.036839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6513` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1381` n `12`; crypto_alt avg `0.18` n `231`; crypto_major avg `0.3165` n `8`; equity avg `-0.0177` n `127`; fx avg `-0.0081` n `6`; index avg `-0.0033` n `26`; metal avg `0.0401` n `20`; unknown avg `-0.0565` n `792`
- 1h: commodity avg `-0.0142` n `12`; crypto_alt avg `0.9217` n `231`; crypto_major avg `1.3821` n `8`; equity avg `0.1542` n `127`; fx avg `-0.0313` n `6`; index avg `0.033` n `26`; metal avg `0.149` n `20`; unknown avg `0.0602` n `792`
- 4h: commodity avg `0.1452` n `12`; crypto_alt avg `1.4157` n `231`; crypto_major avg `1.4303` n `8`; equity avg `-0.221` n `127`; fx avg `0.0203` n `6`; index avg `-0.0274` n `26`; metal avg `0.1135` n `20`; unknown avg `-0.0227` n `792`
- 24h: commodity avg `0.2817` n `12`; crypto_alt avg `3.0039` n `231`; crypto_major avg `3.9379` n `8`; equity avg `1.8927` n `127`; fx avg `-0.0548` n `6`; index avg `0.1888` n `26`; metal avg `-0.1764` n `20`; unknown avg `0.7361` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
