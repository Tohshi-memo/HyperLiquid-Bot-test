# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T18:07:23.638710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.094` n `12`; crypto_alt avg `0.3328` n `228`; crypto_major avg `0.4171` n `8`; equity avg `0.2102` n `74`; fx avg `0.0014` n `6`; index avg `0.1093` n `23`; metal avg `0.1706` n `18`; unknown avg `0.0679` n `517`
- 1h: commodity avg `0.0534` n `12`; crypto_alt avg `0.7138` n `228`; crypto_major avg `0.631` n `8`; equity avg `0.2021` n `74`; fx avg `0.0003` n `6`; index avg `0.0099` n `23`; metal avg `-0.0762` n `18`; unknown avg `-0.037` n `517`
- 4h: commodity avg `0.0851` n `12`; crypto_alt avg `0.9575` n `228`; crypto_major avg `0.6393` n `8`; equity avg `0.8494` n `74`; fx avg `-0.0207` n `6`; index avg `0.1709` n `23`; metal avg `0.4905` n `18`; unknown avg `-0.4277` n `517`
- 24h: commodity avg `-0.5055` n `12`; crypto_alt avg `2.5489` n `228`; crypto_major avg `3.1198` n `8`; equity avg `2.4991` n `74`; fx avg `-0.2826` n `6`; index avg `1.1138` n `23`; metal avg `-0.0028` n `18`; unknown avg `-1.9855` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
