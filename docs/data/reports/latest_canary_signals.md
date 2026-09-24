# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T13:52:30.285780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0366` n `12`; crypto_alt avg `-0.0466` n `234`; crypto_major avg `-0.2266` n `8`; equity avg `-0.1376` n `141`; fx avg `0.0096` n `6`; index avg `-0.0065` n `26`; metal avg `0.0195` n `20`; unknown avg `2.5119` n `943`
- 1h: commodity avg `0.0808` n `12`; crypto_alt avg `1.3307` n `234`; crypto_major avg `0.8354` n `8`; equity avg `0.3603` n `141`; fx avg `0.0011` n `6`; index avg `0.0456` n `26`; metal avg `-0.0272` n `20`; unknown avg `85.9717` n `941`
- 4h: commodity avg `-0.0827` n `12`; crypto_alt avg `1.8389` n `234`; crypto_major avg `1.2195` n `8`; equity avg `0.5854` n `141`; fx avg `-0.0154` n `6`; index avg `0.1053` n `26`; metal avg `0.0674` n `20`; unknown avg `7.2334` n `935`
- 24h: commodity avg `0.4658` n `12`; crypto_alt avg `-2.558` n `234`; crypto_major avg `-2.5973` n `8`; equity avg `-1.4891` n `141`; fx avg `-0.0005` n `6`; index avg `-0.2604` n `26`; metal avg `-0.1006` n `20`; unknown avg `0.3489` n `813`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
