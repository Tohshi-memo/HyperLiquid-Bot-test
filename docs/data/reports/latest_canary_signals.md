# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T01:37:27.530169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `13`; crypto_alt avg `0.3027` n `235`; crypto_major avg `0.1373` n `8`; equity avg `0.0114` n `150`; fx avg `0.0012` n `6`; index avg `-0.0013` n `26`; metal avg `0.0005` n `20`; unknown avg `1.3927` n `1117`
- 1h: commodity avg `-0.0355` n `13`; crypto_alt avg `0.3909` n `235`; crypto_major avg `0.1898` n `8`; equity avg `0.0056` n `150`; fx avg `-0.0014` n `6`; index avg `-0.0047` n `26`; metal avg `0.0022` n `20`; unknown avg `2.3142` n `1115`
- 4h: commodity avg `0.1579` n `13`; crypto_alt avg `-0.0781` n `235`; crypto_major avg `-0.0913` n `8`; equity avg `-0.0443` n `150`; fx avg `0.006` n `6`; index avg `-0.0005` n `26`; metal avg `0.0086` n `20`; unknown avg `5.0607` n `1085`
- 24h: commodity avg `0.0461` n `13`; crypto_alt avg `1.7489` n `235`; crypto_major avg `0.5456` n `8`; equity avg `0.0844` n `150`; fx avg `-0.0098` n `6`; index avg `-0.0165` n `26`; metal avg `-0.0072` n `20`; unknown avg `0.4301` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
