# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T16:37:30.127201+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.4357` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.767` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.072` n `12`; crypto_alt avg `0.2271` n `231`; crypto_major avg `0.0268` n `8`; equity avg `0.0599` n `127`; fx avg `0.0057` n `6`; index avg `0.0323` n `26`; metal avg `0.0307` n `20`; unknown avg `0.502` n `792`
- 1h: commodity avg `0.0811` n `12`; crypto_alt avg `0.553` n `231`; crypto_major avg `0.1678` n `8`; equity avg `0.1341` n `127`; fx avg `0.012` n `6`; index avg `0.0452` n `26`; metal avg `0.1158` n `20`; unknown avg `0.5139` n `792`
- 4h: commodity avg `0.1045` n `12`; crypto_alt avg `1.863` n `231`; crypto_major avg `2.0457` n `8`; equity avg `-0.39` n `127`; fx avg `0.0236` n `6`; index avg `-0.0155` n `26`; metal avg `0.2787` n `20`; unknown avg `0.1136` n `792`
- 24h: commodity avg `-0.0039` n `12`; crypto_alt avg `4.8405` n `231`; crypto_major avg `5.2277` n `8`; equity avg `1.8221` n `127`; fx avg `-0.0557` n `6`; index avg `0.2305` n `26`; metal avg `0.1654` n `20`; unknown avg `0.958` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
