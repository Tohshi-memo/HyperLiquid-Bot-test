# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T12:22:30.068594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `13`; crypto_alt avg `-0.0267` n `235`; crypto_major avg `-0.1358` n `8`; equity avg `-0.0014` n `150`; fx avg `-0.0118` n `6`; index avg `0.0021` n `26`; metal avg `0.0062` n `20`; unknown avg `1.1762` n `1078`
- 1h: commodity avg `0.0297` n `13`; crypto_alt avg `0.3868` n `235`; crypto_major avg `0.5318` n `8`; equity avg `0.0627` n `150`; fx avg `-0.0152` n `6`; index avg `0.013` n `26`; metal avg `-0.0129` n `20`; unknown avg `1.0873` n `1070`
- 4h: commodity avg `0.0767` n `13`; crypto_alt avg `-0.348` n `235`; crypto_major avg `0.0386` n `8`; equity avg `-0.0721` n `150`; fx avg `-0.0997` n `6`; index avg `-0.025` n `26`; metal avg `-0.1034` n `20`; unknown avg `1.7696` n `1070`
- 24h: commodity avg `-0.5744` n `13`; crypto_alt avg `-0.9954` n `235`; crypto_major avg `-0.7861` n `8`; equity avg `-0.1117` n `150`; fx avg `0.0113` n `6`; index avg `0.0602` n `26`; metal avg `0.518` n `20`; unknown avg `7.4368` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
