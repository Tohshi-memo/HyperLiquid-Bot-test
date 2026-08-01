# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T13:22:27.315372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `-0.09` n `230`; crypto_major avg `0.0193` n `8`; equity avg `-0.0239` n `102`; fx avg `0.0018` n `6`; index avg `-0.0128` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.0243` n `782`
- 1h: commodity avg `0.0435` n `12`; crypto_alt avg `-0.1163` n `230`; crypto_major avg `0.0173` n `8`; equity avg `-0.0983` n `102`; fx avg `0.0237` n `6`; index avg `-0.0017` n `25`; metal avg `0.0086` n `20`; unknown avg `-0.0557` n `782`
- 4h: commodity avg `0.0976` n `12`; crypto_alt avg `-0.0906` n `230`; crypto_major avg `-0.1039` n `8`; equity avg `-0.1059` n `102`; fx avg `-0.0685` n `6`; index avg `0.0036` n `25`; metal avg `0.0052` n `20`; unknown avg `-0.1006` n `781`
- 24h: commodity avg `0.4219` n `12`; crypto_alt avg `0.0338` n `230`; crypto_major avg `-1.5225` n `8`; equity avg `-2.6874` n `102`; fx avg `-0.1082` n `6`; index avg `-0.2782` n `25`; metal avg `0.0925` n `20`; unknown avg `4.2626` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
