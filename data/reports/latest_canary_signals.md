# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T14:52:12.536869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `0.1491` n `228`; crypto_major avg `0.0895` n `8`; equity avg `-0.0052` n `65`; fx avg `0.0` n `5`; index avg `0.0043` n `23`; metal avg `-0.0116` n `18`; unknown avg `0.0161` n `383`
- 1h: commodity avg `-0.0963` n `12`; crypto_alt avg `-0.1692` n `228`; crypto_major avg `-0.1551` n `8`; equity avg `-0.002` n `65`; fx avg `0.0215` n `5`; index avg `-0.0448` n `23`; metal avg `-0.0615` n `18`; unknown avg `0.0745` n `383`
- 4h: commodity avg `-0.056` n `12`; crypto_alt avg `-0.6696` n `228`; crypto_major avg `-0.4535` n `8`; equity avg `0.0147` n `65`; fx avg `0.0033` n `5`; index avg `0.0214` n `23`; metal avg `-0.0497` n `18`; unknown avg `-0.0844` n `383`
- 24h: commodity avg `1.7058` n `12`; crypto_alt avg `-9.2813` n `228`; crypto_major avg `-2.5572` n `8`; equity avg `-2.6224` n `65`; fx avg `-0.1649` n `5`; index avg `-1.6445` n `23`; metal avg `-5.8746` n `18`; unknown avg `549.9967` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
