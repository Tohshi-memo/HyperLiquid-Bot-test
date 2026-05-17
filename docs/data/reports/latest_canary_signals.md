# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T21:06:27.531115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.052` n `12`; crypto_alt avg `-0.0514` n `228`; crypto_major avg `-0.0078` n `8`; equity avg `-0.0537` n `65`; fx avg `-0.0243` n `5`; index avg `-0.0253` n `23`; metal avg `-0.0235` n `18`; unknown avg `0.1345` n `384`
- 1h: commodity avg `-0.1052` n `12`; crypto_alt avg `-0.114` n `228`; crypto_major avg `-0.1751` n `8`; equity avg `-0.0177` n `65`; fx avg `-0.0272` n `5`; index avg `-0.0026` n `23`; metal avg `-0.017` n `18`; unknown avg `-0.2983` n `384`
- 4h: commodity avg `-0.0864` n `12`; crypto_alt avg `0.3737` n `228`; crypto_major avg `1.1691` n `8`; equity avg `0.4324` n `65`; fx avg `-0.0278` n `5`; index avg `0.136` n `23`; metal avg `-0.1262` n `18`; unknown avg `0.3995` n `384`
- 24h: commodity avg `1.6948` n `12`; crypto_alt avg `-9.2141` n `228`; crypto_major avg `-1.3629` n `8`; equity avg `-2.2756` n `65`; fx avg `-0.1818` n `5`; index avg `-1.5095` n `23`; metal avg `-5.9718` n `18`; unknown avg `550.4231` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
