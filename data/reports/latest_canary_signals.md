# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T00:52:29.607470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0582` n `13`; crypto_alt avg `-0.1061` n `235`; crypto_major avg `0.0724` n `8`; equity avg `-0.246` n `150`; fx avg `-0.0197` n `6`; index avg `-0.0584` n `26`; metal avg `0.002` n `20`; unknown avg `0.1009` n `1126`
- 1h: commodity avg `-0.028` n `13`; crypto_alt avg `-0.2556` n `235`; crypto_major avg `0.0876` n `8`; equity avg `-0.0652` n `150`; fx avg `-0.0544` n `6`; index avg `-0.0407` n `26`; metal avg `0.089` n `20`; unknown avg `0.0668` n `1118`
- 4h: commodity avg `-0.4183` n `13`; crypto_alt avg `-0.0256` n `235`; crypto_major avg `0.1422` n `8`; equity avg `0.031` n `150`; fx avg `-0.0616` n `6`; index avg `-0.0234` n `26`; metal avg `0.0792` n `20`; unknown avg `0.0543` n `1090`
- 24h: commodity avg `-0.28` n `13`; crypto_alt avg `2.2673` n `235`; crypto_major avg `1.1381` n `8`; equity avg `0.3419` n `150`; fx avg `-0.0376` n `6`; index avg `0.0094` n `26`; metal avg `0.1557` n `20`; unknown avg `0.7094` n `949`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
