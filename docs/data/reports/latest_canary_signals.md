# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T11:04:01.686747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `0.0694` n `230`; crypto_major avg `-0.0424` n `8`; equity avg `0.0067` n `102`; fx avg `0.0` n `6`; index avg `-0.0046` n `25`; metal avg `-0.0066` n `20`; unknown avg `-0.0035` n `781`
- 1h: commodity avg `-0.0272` n `12`; crypto_alt avg `0.1176` n `230`; crypto_major avg `-0.0023` n `8`; equity avg `0.0169` n `102`; fx avg `-0.0421` n `6`; index avg `0.0259` n `25`; metal avg `0.0122` n `20`; unknown avg `0.0008` n `781`
- 4h: commodity avg `0.033` n `12`; crypto_alt avg `-0.3379` n `230`; crypto_major avg `-0.3478` n `8`; equity avg `-0.0181` n `102`; fx avg `-0.0224` n `6`; index avg `0.0506` n `25`; metal avg `0.0069` n `20`; unknown avg `-0.0345` n `781`
- 24h: commodity avg `0.4929` n `12`; crypto_alt avg `0.0973` n `230`; crypto_major avg `-1.4606` n `8`; equity avg `-2.9404` n `102`; fx avg `-0.1187` n `6`; index avg `-0.2887` n `25`; metal avg `-0.0466` n `20`; unknown avg `4.6085` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
