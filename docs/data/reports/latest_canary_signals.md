# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T12:15:20.924241+00:00`
- Correlation status: `ready`
- Asset price records: `168`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `7`; crypto_alt avg `0.226` n `223`; crypto_major avg `0.1853` n `7`; equity avg `-0.0078` n `42`; fx avg `0.0037` n `4`; index avg `0.0` n `9`; metal avg `-0.009` n `7`; unknown avg `-0.3464` n `313`
- 1h: commodity avg `0.0069` n `7`; crypto_alt avg `0.3297` n `223`; crypto_major avg `0.4666` n `7`; equity avg `-0.002` n `42`; fx avg `-0.0016` n `4`; index avg `0.0382` n `9`; metal avg `0.0204` n `7`; unknown avg `0.0925` n `313`
- 4h: commodity avg `-0.0601` n `7`; crypto_alt avg `0.3258` n `223`; crypto_major avg `0.6115` n `7`; equity avg `0.0966` n `42`; fx avg `0.008` n `4`; index avg `-0.0018` n `9`; metal avg `0.0678` n `7`; unknown avg `0.1018` n `313`
- 24h: commodity avg `-0.2216` n `7`; crypto_alt avg `1.4963` n `223`; crypto_major avg `0.609` n `7`; equity avg `0.3589` n `42`; fx avg `0.1409` n `4`; index avg `0.0674` n `9`; metal avg `0.1395` n `7`; unknown avg `0.2095` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `164`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3952`, n `164`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `164`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3812`, n `164`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3796`, n `160`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3739`, n `160`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3625`, n `160`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3546`, n `160`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.328`, n `164`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3149`, n `164`, moderate_sample_signal
