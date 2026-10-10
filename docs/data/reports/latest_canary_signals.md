# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T10:07:26.185165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `13`; crypto_alt avg `-0.1638` n `235`; crypto_major avg `-0.0915` n `8`; equity avg `-0.0049` n `150`; fx avg `0.0018` n `6`; index avg `0.0011` n `26`; metal avg `0.003` n `20`; unknown avg `0.0612` n `1115`
- 1h: commodity avg `-0.2224` n `13`; crypto_alt avg `-0.1967` n `235`; crypto_major avg `-0.1539` n `8`; equity avg `0.0046` n `150`; fx avg `0.0023` n `6`; index avg `0.0145` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.1678` n `1115`
- 4h: commodity avg `-0.2388` n `13`; crypto_alt avg `-0.4323` n `235`; crypto_major avg `-0.1222` n `8`; equity avg `-0.0541` n `150`; fx avg `-0.0095` n `6`; index avg `-0.0226` n `26`; metal avg `0.0067` n `20`; unknown avg `1.7318` n `1098`
- 24h: commodity avg `-0.1259` n `13`; crypto_alt avg `1.2188` n `235`; crypto_major avg `-0.0877` n `8`; equity avg `-0.252` n `150`; fx avg `-0.0345` n `6`; index avg `-0.0281` n `26`; metal avg `0.0582` n `20`; unknown avg `632.112` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
