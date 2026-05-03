# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T19:15:40.909379+00:00`
- Correlation status: `ready`
- Asset price records: `196`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0357` n `7`; crypto_alt avg `0.0056` n `223`; crypto_major avg `-0.0259` n `7`; equity avg `-0.016` n `42`; fx avg `0.0032` n `4`; index avg `0.0016` n `9`; metal avg `0.0404` n `7`; unknown avg `-0.0431` n `314`
- 1h: commodity avg `0.1121` n `7`; crypto_alt avg `0.1716` n `223`; crypto_major avg `0.0858` n `7`; equity avg `0.0844` n `42`; fx avg `-0.0151` n `4`; index avg `0.0171` n `9`; metal avg `-0.0398` n `7`; unknown avg `0.0059` n `314`
- 4h: commodity avg `0.2073` n `7`; crypto_alt avg `0.0942` n `223`; crypto_major avg `-0.0101` n `7`; equity avg `0.2414` n `42`; fx avg `-0.0373` n `4`; index avg `0.082` n `9`; metal avg `0.1825` n `7`; unknown avg `0.2035` n `313`
- 24h: commodity avg `-0.0518` n `7`; crypto_alt avg `-0.1606` n `223`; crypto_major avg `-0.0775` n `7`; equity avg `0.3964` n `42`; fx avg `0.0469` n `4`; index avg `0.0531` n `9`; metal avg `0.4623` n `7`; unknown avg `0.0245` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.399`, n `192`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3811`, n `192`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3764`, n `192`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3753`, n `188`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.368`, n `188`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.363`, n `192`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.329`, n `192`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3101`, n `192`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.305`, n `192`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2592`, n `188`, moderate_sample_signal
