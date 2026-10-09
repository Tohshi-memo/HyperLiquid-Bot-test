# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T17:22:31.157951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0377` n `13`; crypto_alt avg `-0.2942` n `235`; crypto_major avg `-0.1965` n `8`; equity avg `0.0045` n `150`; fx avg `0.011` n `6`; index avg `-0.0086` n `26`; metal avg `0.0183` n `20`; unknown avg `-0.0242` n `1092`
- 1h: commodity avg `-0.1009` n `13`; crypto_alt avg `-0.3273` n `235`; crypto_major avg `-0.2263` n `8`; equity avg `0.116` n `150`; fx avg `0.0197` n `6`; index avg `-0.0013` n `26`; metal avg `0.0063` n `20`; unknown avg `1.9269` n `1082`
- 4h: commodity avg `0.1099` n `13`; crypto_alt avg `0.0529` n `235`; crypto_major avg `-0.5071` n `8`; equity avg `-0.4171` n `150`; fx avg `0.0186` n `6`; index avg `-0.0379` n `26`; metal avg `0.0485` n `20`; unknown avg `-0.0055` n `996`
- 24h: commodity avg `0.1626` n `13`; crypto_alt avg `4.0549` n `235`; crypto_major avg `2.4574` n `8`; equity avg `1.4909` n `150`; fx avg `0.0423` n `6`; index avg `0.2166` n `26`; metal avg `0.5594` n `20`; unknown avg `1.8183` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
