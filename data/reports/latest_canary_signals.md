# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T06:37:31.389958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.3768` n `234`; crypto_major avg `-0.303` n `8`; equity avg `-0.0412` n `141`; fx avg `0.0033` n `6`; index avg `0.0018` n `26`; metal avg `-0.0171` n `20`; unknown avg `3.2072` n `946`
- 1h: commodity avg `-0.0521` n `12`; crypto_alt avg `0.0094` n `234`; crypto_major avg `-0.1902` n `8`; equity avg `0.1808` n `141`; fx avg `-0.0001` n `6`; index avg `0.0318` n `26`; metal avg `0.03` n `20`; unknown avg `3.2499` n `912`
- 4h: commodity avg `-0.0374` n `12`; crypto_alt avg `0.0001` n `234`; crypto_major avg `-0.4351` n `8`; equity avg `0.4386` n `141`; fx avg `-0.0471` n `6`; index avg `0.0959` n `26`; metal avg `-0.0177` n `20`; unknown avg `1.4542` n `906`
- 24h: commodity avg `0.1837` n `12`; crypto_alt avg `1.5621` n `234`; crypto_major avg `0.1067` n `8`; equity avg `1.1069` n `141`; fx avg `-0.1808` n `6`; index avg `0.1796` n `26`; metal avg `-0.0925` n `20`; unknown avg `15.2086` n `799`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
