# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T21:37:11.741546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `0.0449` n `228`; crypto_major avg `0.0485` n `8`; equity avg `-0.0394` n `65`; fx avg `0.0` n `5`; index avg `0.0243` n `23`; metal avg `0.0212` n `18`; unknown avg `0.2338` n `376`
- 1h: commodity avg `0.0064` n `12`; crypto_alt avg `0.1249` n `228`; crypto_major avg `0.0559` n `8`; equity avg `0.006` n `65`; fx avg `-0.0289` n `5`; index avg `0.0547` n `23`; metal avg `0.036` n `18`; unknown avg `0.2212` n `376`
- 4h: commodity avg `0.0125` n `12`; crypto_alt avg `-0.0806` n `228`; crypto_major avg `-0.0678` n `8`; equity avg `0.2431` n `65`; fx avg `-0.0117` n `5`; index avg `0.0469` n `23`; metal avg `0.1635` n `18`; unknown avg `0.1238` n `376`
- 24h: commodity avg `0.317` n `12`; crypto_alt avg `0.2697` n `228`; crypto_major avg `0.3416` n `8`; equity avg `0.6672` n `65`; fx avg `-0.0268` n `5`; index avg `0.4041` n `23`; metal avg `0.0793` n `18`; unknown avg `0.2325` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
