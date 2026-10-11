# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T02:22:28.489602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `13`; crypto_alt avg `0.0814` n `235`; crypto_major avg `0.0517` n `8`; equity avg `0.002` n `150`; fx avg `0.0045` n `6`; index avg `0.0011` n `26`; metal avg `0.0057` n `20`; unknown avg `-0.0259` n `1117`
- 1h: commodity avg `0.013` n `13`; crypto_alt avg `0.387` n `235`; crypto_major avg `0.128` n `8`; equity avg `0.0208` n `150`; fx avg `0.0076` n `6`; index avg `0.0047` n `26`; metal avg `0.0051` n `20`; unknown avg `-0.167` n `1115`
- 4h: commodity avg `0.0194` n `13`; crypto_alt avg `0.1728` n `235`; crypto_major avg `-0.0152` n `8`; equity avg `-0.0396` n `150`; fx avg `0.0063` n `6`; index avg `-0.001` n `26`; metal avg `0.0062` n `20`; unknown avg `2.7534` n `1109`
- 24h: commodity avg `0.128` n `13`; crypto_alt avg `1.4172` n `235`; crypto_major avg `0.3845` n `8`; equity avg `0.1106` n `150`; fx avg `-0.0007` n `6`; index avg `-0.0047` n `26`; metal avg `0.001` n `20`; unknown avg `0.3158` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
