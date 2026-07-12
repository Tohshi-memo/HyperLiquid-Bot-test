# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T01:22:30.567263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3525` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0882` n `12`; crypto_alt avg `0.2802` n `230`; crypto_major avg `0.2603` n `8`; equity avg `0.102` n `92`; fx avg `0.003` n `6`; index avg `0.0095` n `25`; metal avg `0.0111` n `20`; unknown avg `-0.0537` n `765`
- 1h: commodity avg `-0.0697` n `12`; crypto_alt avg `0.2076` n `230`; crypto_major avg `0.2139` n `8`; equity avg `-0.0194` n `92`; fx avg `0.0002` n `6`; index avg `-0.0233` n `25`; metal avg `-0.0189` n `20`; unknown avg `0.0682` n `765`
- 4h: commodity avg `0.4599` n `12`; crypto_alt avg `-1.6367` n `230`; crypto_major avg `-1.4655` n `8`; equity avg `-0.2718` n `92`; fx avg `0.0159` n `6`; index avg `-0.113` n `25`; metal avg `-0.0454` n `20`; unknown avg `1.0385` n `765`
- 24h: commodity avg `0.4474` n `12`; crypto_alt avg `-0.9148` n `229`; crypto_major avg `-0.7748` n `8`; equity avg `0.0022` n `92`; fx avg `0.0189` n `6`; index avg `-0.086` n `25`; metal avg `-0.0763` n `20`; unknown avg `-0.4034` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
