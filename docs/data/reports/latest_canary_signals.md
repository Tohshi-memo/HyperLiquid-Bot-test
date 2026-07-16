# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T13:37:32.257303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0332` n `12`; crypto_alt avg `0.177` n `230`; crypto_major avg `0.1815` n `8`; equity avg `-0.3195` n `94`; fx avg `0.0122` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0366` n `20`; unknown avg `0.0525` n `768`
- 1h: commodity avg `-0.0756` n `12`; crypto_alt avg `0.5595` n `230`; crypto_major avg `0.5958` n `8`; equity avg `-0.0551` n `94`; fx avg `0.029` n `6`; index avg `0.0853` n `25`; metal avg `-0.0367` n `20`; unknown avg `0.1497` n `768`
- 4h: commodity avg `0.3012` n `12`; crypto_alt avg `0.5865` n `230`; crypto_major avg `0.2604` n `8`; equity avg `-0.9126` n `94`; fx avg `0.0195` n `6`; index avg `-0.1454` n `25`; metal avg `-0.3171` n `20`; unknown avg `0.1347` n `768`
- 24h: commodity avg `0.2864` n `12`; crypto_alt avg `-1.4094` n `230`; crypto_major avg `-2.0384` n `8`; equity avg `-3.3977` n `93`; fx avg `0.0379` n `6`; index avg `-0.5441` n `25`; metal avg `-0.5074` n `20`; unknown avg `-0.1711` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
