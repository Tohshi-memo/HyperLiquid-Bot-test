# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T18:37:24.542594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `0.1402` n `231`; crypto_major avg `0.1198` n `8`; equity avg `0.0236` n `122`; fx avg `-0.0106` n `6`; index avg `0.0049` n `25`; metal avg `0.023` n `20`; unknown avg `0.0495` n `793`
- 1h: commodity avg `-0.0234` n `12`; crypto_alt avg `0.2735` n `231`; crypto_major avg `0.273` n `8`; equity avg `0.0858` n `122`; fx avg `-0.0097` n `6`; index avg `0.0369` n `25`; metal avg `0.0226` n `20`; unknown avg `0.2741` n `793`
- 4h: commodity avg `-0.0417` n `12`; crypto_alt avg `1.8158` n `231`; crypto_major avg `0.8799` n `8`; equity avg `0.3246` n `122`; fx avg `0.004` n `6`; index avg `0.0529` n `25`; metal avg `0.0722` n `20`; unknown avg `0.7747` n `793`
- 24h: commodity avg `-0.0161` n `12`; crypto_alt avg `2.1629` n `231`; crypto_major avg `0.6339` n `8`; equity avg `0.7616` n `122`; fx avg `0.0254` n `6`; index avg `0.1111` n `25`; metal avg `0.0986` n `20`; unknown avg `5.5139` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
