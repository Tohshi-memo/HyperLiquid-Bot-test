# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T18:22:17.373480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0486` n `12`; crypto_alt avg `-0.3739` n `228`; crypto_major avg `-0.2103` n `8`; equity avg `-0.0126` n `65`; fx avg `-0.0013` n `5`; index avg `0.0154` n `23`; metal avg `-0.0083` n `18`; unknown avg `-0.1646` n `384`
- 1h: commodity avg `0.0684` n `12`; crypto_alt avg `-0.2212` n `228`; crypto_major avg `0.1286` n `8`; equity avg `0.0318` n `65`; fx avg `-0.0013` n `5`; index avg `0.0527` n `23`; metal avg `-0.0381` n `18`; unknown avg `0.0419` n `384`
- 4h: commodity avg `0.2586` n `12`; crypto_alt avg `-0.2732` n `228`; crypto_major avg `0.1559` n `8`; equity avg `0.0851` n `65`; fx avg `0.031` n `5`; index avg `0.0512` n `23`; metal avg `-0.062` n `18`; unknown avg `-0.0962` n `383`
- 24h: commodity avg `1.8203` n `12`; crypto_alt avg `-9.8336` n `228`; crypto_major avg `-2.5628` n `8`; equity avg `-2.6213` n `65`; fx avg `-0.1555` n `5`; index avg `-1.5823` n `23`; metal avg `-5.893` n `18`; unknown avg `549.9478` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
