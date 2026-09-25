# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T19:52:32.213730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0178` n `12`; crypto_alt avg `0.0195` n `234`; crypto_major avg `-0.0123` n `8`; equity avg `0.068` n `141`; fx avg `0.0044` n `6`; index avg `0.0327` n `26`; metal avg `-0.018` n `20`; unknown avg `312.186` n `960`
- 1h: commodity avg `0.128` n `12`; crypto_alt avg `0.003` n `234`; crypto_major avg `0.0244` n `8`; equity avg `-0.0217` n `141`; fx avg `0.0063` n `6`; index avg `0.0312` n `26`; metal avg `-0.0347` n `20`; unknown avg `121.7533` n `958`
- 4h: commodity avg `-0.2715` n `12`; crypto_alt avg `1.5536` n `234`; crypto_major avg `0.9201` n `8`; equity avg `0.4531` n `141`; fx avg `-0.0105` n `6`; index avg `0.1858` n `26`; metal avg `0.1553` n `20`; unknown avg `9.7097` n `942`
- 24h: commodity avg `-0.9035` n `12`; crypto_alt avg `1.8916` n `234`; crypto_major avg `0.5154` n `8`; equity avg `0.0559` n `141`; fx avg `-0.249` n `6`; index avg `0.2249` n `26`; metal avg `0.1339` n `20`; unknown avg `1549.6029` n `834`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
