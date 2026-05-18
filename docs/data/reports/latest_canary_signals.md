# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T08:22:18.115069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1857` n `12`; crypto_alt avg `-0.1343` n `228`; crypto_major avg `-0.0986` n `8`; equity avg `0.2009` n `66`; fx avg `-0.0059` n `5`; index avg `0.0708` n `23`; metal avg `0.0347` n `18`; unknown avg `-0.0528` n `383`
- 1h: commodity avg `-0.0196` n `12`; crypto_alt avg `0.2489` n `228`; crypto_major avg `0.3032` n `8`; equity avg `0.5763` n `66`; fx avg `-0.0388` n `5`; index avg `0.2369` n `23`; metal avg `0.2624` n `18`; unknown avg `0.0796` n `383`
- 4h: commodity avg `-0.2066` n `12`; crypto_alt avg `-0.6388` n `228`; crypto_major avg `-0.3507` n `8`; equity avg `0.5528` n `66`; fx avg `-0.0782` n `5`; index avg `0.1363` n `23`; metal avg `0.2971` n `18`; unknown avg `-0.1955` n `363`
- 24h: commodity avg `0.7626` n `12`; crypto_alt avg `-2.8753` n `228`; crypto_major avg `-1.2498` n `8`; equity avg `0.4981` n `65`; fx avg `0.0316` n `5`; index avg `0.271` n `23`; metal avg `0.0525` n `18`; unknown avg `-0.4075` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
