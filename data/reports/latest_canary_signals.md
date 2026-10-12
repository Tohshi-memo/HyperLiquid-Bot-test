# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T08:07:29.473471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.11` n `13`; crypto_alt avg `-0.2188` n `235`; crypto_major avg `-0.1625` n `8`; equity avg `-0.1237` n `151`; fx avg `-0.0072` n `6`; index avg `-0.0197` n `26`; metal avg `-0.0535` n `20`; unknown avg `0.0859` n `1059`
- 1h: commodity avg `-0.0346` n `13`; crypto_alt avg `-0.1792` n `235`; crypto_major avg `-0.2315` n `8`; equity avg `-0.003` n `151`; fx avg `-0.0305` n `6`; index avg `0.0169` n `26`; metal avg `-0.0506` n `20`; unknown avg `0.1361` n `1059`
- 4h: commodity avg `0.1193` n `13`; crypto_alt avg `0.1919` n `235`; crypto_major avg `0.5095` n `8`; equity avg `-0.3541` n `151`; fx avg `-0.0384` n `6`; index avg `-0.0564` n `26`; metal avg `-0.0863` n `20`; unknown avg `0.2219` n `981`
- 24h: commodity avg `-0.3667` n `13`; crypto_alt avg `2.4641` n `235`; crypto_major avg `1.827` n `8`; equity avg `-0.6078` n `151`; fx avg `-0.1044` n `6`; index avg `-0.0434` n `26`; metal avg `0.0397` n `20`; unknown avg `0.2494` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2078`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
