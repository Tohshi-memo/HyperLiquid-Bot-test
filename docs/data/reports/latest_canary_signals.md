# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T09:00:25.681301+00:00`
- Correlation status: `ready`
- Asset price records: `155`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `7`; crypto_alt avg `0.0075` n `223`; crypto_major avg `0.0181` n `7`; equity avg `0.0128` n `42`; fx avg `0.0027` n `4`; index avg `-0.0485` n `9`; metal avg `-0.0001` n `7`; unknown avg `0.0152` n `313`
- 1h: commodity avg `0.0141` n `7`; crypto_alt avg `0.197` n `223`; crypto_major avg `0.0916` n `7`; equity avg `-0.1379` n `42`; fx avg `0.0064` n `4`; index avg `-0.0057` n `9`; metal avg `0.0459` n `7`; unknown avg `-0.0797` n `313`
- 4h: commodity avg `-0.0676` n `7`; crypto_alt avg `0.5076` n `223`; crypto_major avg `0.2639` n `7`; equity avg `-0.193` n `42`; fx avg `0.0202` n `4`; index avg `0.002` n `9`; metal avg `0.1062` n `7`; unknown avg `0.2822` n `311`
- 24h: commodity avg `-0.2109` n `7`; crypto_alt avg `1.3309` n `223`; crypto_major avg `-0.1241` n `7`; equity avg `0.1775` n `42`; fx avg `0.1297` n `4`; index avg `0.0231` n `9`; metal avg `0.108` n `7`; unknown avg `0.1862` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4242`, n `151`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4095`, n `151`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4033`, n `151`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3879`, n `147`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3855`, n `151`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3825`, n `147`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3761`, n `147`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3686`, n `147`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3527`, n `151`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3505`, n `151`, moderate_sample_signal
