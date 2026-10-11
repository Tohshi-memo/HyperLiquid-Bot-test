# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T08:52:23.356640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `13`; crypto_alt avg `-0.0346` n `235`; crypto_major avg `0.0082` n `8`; equity avg `0.0237` n `150`; fx avg `0.0005` n `6`; index avg `0.0028` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.1522` n `1117`
- 1h: commodity avg `0.0169` n `13`; crypto_alt avg `0.1497` n `235`; crypto_major avg `0.0966` n `8`; equity avg `0.0248` n `150`; fx avg `-0.0011` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0062` n `20`; unknown avg `-0.0394` n `1099`
- 4h: commodity avg `0.0219` n `13`; crypto_alt avg `0.5473` n `235`; crypto_major avg `-0.1209` n `8`; equity avg `0.0338` n `150`; fx avg `-0.0039` n `6`; index avg `0.0063` n `26`; metal avg `0.0137` n `20`; unknown avg `0.3429` n `1083`
- 24h: commodity avg `0.1899` n `13`; crypto_alt avg `1.1751` n `235`; crypto_major avg `-0.1739` n `8`; equity avg `0.0803` n `150`; fx avg `-0.0002` n `6`; index avg `0.0013` n `26`; metal avg `0.0006` n `20`; unknown avg `0.5749` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
