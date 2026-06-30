# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T16:52:30.170252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.28` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `0.2307` n `228`; crypto_major avg `0.3697` n `8`; equity avg `0.1841` n `88`; fx avg `0.0027` n `6`; index avg `0.0199` n `23`; metal avg `0.0196` n `20`; unknown avg `0.1582` n `765`
- 1h: commodity avg `0.0587` n `12`; crypto_alt avg `-0.0756` n `228`; crypto_major avg `-0.022` n `8`; equity avg `0.4805` n `88`; fx avg `-0.0153` n `6`; index avg `0.0591` n `23`; metal avg `0.0225` n `20`; unknown avg `-0.0162` n `765`
- 4h: commodity avg `-0.0612` n `12`; crypto_alt avg `0.7968` n `228`; crypto_major avg `0.5948` n `8`; equity avg `1.1854` n `88`; fx avg `0.0709` n `6`; index avg `0.2484` n `23`; metal avg `0.1973` n `20`; unknown avg `-0.095` n `765`
- 24h: commodity avg `0.1772` n `12`; crypto_alt avg `-1.7004` n `228`; crypto_major avg `-1.1838` n `8`; equity avg `1.7258` n `88`; fx avg `0.131` n `6`; index avg `0.4016` n `23`; metal avg `0.4766` n `20`; unknown avg `8.5573` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
