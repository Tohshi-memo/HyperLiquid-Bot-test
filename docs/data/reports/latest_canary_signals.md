# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T13:07:29.759391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `13`; crypto_alt avg `0.0193` n `235`; crypto_major avg `-0.0536` n `8`; equity avg `-0.0178` n `150`; fx avg `0.0007` n `6`; index avg `0.0022` n `26`; metal avg `0.0023` n `20`; unknown avg `0.0255` n `1083`
- 1h: commodity avg `0.0144` n `13`; crypto_alt avg `0.0654` n `235`; crypto_major avg `-0.183` n `8`; equity avg `-0.0082` n `150`; fx avg `-0.0079` n `6`; index avg `0.0008` n `26`; metal avg `0.0029` n `20`; unknown avg `0.4475` n `1059`
- 4h: commodity avg `-0.0326` n `13`; crypto_alt avg `0.012` n `235`; crypto_major avg `-0.0059` n `8`; equity avg `0.0832` n `150`; fx avg `0.0274` n `6`; index avg `0.0089` n `26`; metal avg `0.0001` n `20`; unknown avg `0.5825` n `1053`
- 24h: commodity avg `0.3178` n `13`; crypto_alt avg `1.3387` n `235`; crypto_major avg `-0.0352` n `8`; equity avg `0.1488` n `150`; fx avg `0.0203` n `6`; index avg `0.009` n `26`; metal avg `0.0152` n `20`; unknown avg `0.5915` n `941`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
