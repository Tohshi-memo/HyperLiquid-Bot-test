# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T10:52:29.209248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1549` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0359` n `12`; crypto_alt avg `0.4663` n `234`; crypto_major avg `0.5053` n `8`; equity avg `0.1517` n `141`; fx avg `-0.0045` n `6`; index avg `0.0445` n `26`; metal avg `-0.0117` n `20`; unknown avg `1.3449` n `945`
- 1h: commodity avg `-0.1314` n `12`; crypto_alt avg `0.0887` n `234`; crypto_major avg `0.2231` n `8`; equity avg `0.4013` n `141`; fx avg `0.0147` n `6`; index avg `0.073` n `26`; metal avg `0.0225` n `20`; unknown avg `0.6733` n `943`
- 4h: commodity avg `0.0765` n `12`; crypto_alt avg `-1.5851` n `234`; crypto_major avg `-1.1944` n `8`; equity avg `-0.3531` n `141`; fx avg `0.0249` n `6`; index avg `-0.0395` n `26`; metal avg `-0.1137` n `20`; unknown avg `2.5673` n `937`
- 24h: commodity avg `0.5906` n `12`; crypto_alt avg `-5.0992` n `234`; crypto_major avg `-3.9305` n `8`; equity avg `-2.387` n `141`; fx avg `0.0386` n `6`; index avg `-0.4353` n `26`; metal avg `-0.4859` n `20`; unknown avg `586.8659` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
