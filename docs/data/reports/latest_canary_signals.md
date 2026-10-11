# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T05:52:27.127259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0049` n `13`; crypto_alt avg `0.056` n `235`; crypto_major avg `-0.0508` n `8`; equity avg `-0.0198` n `150`; fx avg `-0.0007` n `6`; index avg `-0.001` n `26`; metal avg `0.0006` n `20`; unknown avg `-0.2925` n `1117`
- 1h: commodity avg `-0.0363` n `13`; crypto_alt avg `0.118` n `235`; crypto_major avg `-0.1357` n `8`; equity avg `-0.0128` n `150`; fx avg `-0.0055` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.1598` n `1115`
- 4h: commodity avg `0.0906` n `13`; crypto_alt avg `-0.7185` n `235`; crypto_major avg `-0.3757` n `8`; equity avg `-0.1067` n `150`; fx avg `0.0011` n `6`; index avg `-0.0144` n `26`; metal avg `-0.0086` n `20`; unknown avg `-0.1096` n `1109`
- 24h: commodity avg `0.1226` n `13`; crypto_alt avg `0.3395` n `235`; crypto_major avg `-0.2736` n `8`; equity avg `-0.0527` n `150`; fx avg `-0.0122` n `6`; index avg `-0.0411` n `26`; metal avg `-0.004` n `20`; unknown avg `0.3596` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
