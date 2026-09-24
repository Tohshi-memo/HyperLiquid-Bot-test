# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T08:52:28.889735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.235` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0266` n `12`; crypto_alt avg `-0.3506` n `234`; crypto_major avg `-0.3928` n `8`; equity avg `-0.1508` n `141`; fx avg `0.0011` n `6`; index avg `-0.0173` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.045` n `945`
- 1h: commodity avg `0.3726` n `12`; crypto_alt avg `-1.3372` n `234`; crypto_major avg `-1.3725` n `8`; equity avg `-0.9749` n `141`; fx avg `0.0585` n `6`; index avg `-0.1375` n `26`; metal avg `-0.192` n `20`; unknown avg `1.6545` n `937`
- 4h: commodity avg `0.5181` n `12`; crypto_alt avg `-0.5871` n `234`; crypto_major avg `-0.4923` n `8`; equity avg `-1.0253` n `141`; fx avg `0.0381` n `6`; index avg `-0.1636` n `26`; metal avg `-0.1275` n `20`; unknown avg `3.6488` n `921`
- 24h: commodity avg `0.8617` n `12`; crypto_alt avg `-4.0436` n `234`; crypto_major avg `-3.4269` n `8`; equity avg `-2.7253` n `140`; fx avg `0.0229` n `6`; index avg `-0.498` n `26`; metal avg `-0.4962` n `20`; unknown avg `588.5819` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
