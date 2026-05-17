# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T20:22:26.502021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0318` n `12`; crypto_alt avg `-0.1334` n `228`; crypto_major avg `-0.2888` n `8`; equity avg `-0.0195` n `65`; fx avg `0.003` n `5`; index avg `0.0301` n `23`; metal avg `0.0109` n `18`; unknown avg `-0.3416` n `384`
- 1h: commodity avg `-0.0449` n `12`; crypto_alt avg `0.0596` n `228`; crypto_major avg `0.1208` n `8`; equity avg `0.1517` n `65`; fx avg `0.003` n `5`; index avg `0.112` n `23`; metal avg `-0.0012` n `18`; unknown avg `-0.2573` n `384`
- 4h: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.0739` n `228`; crypto_major avg `0.8596` n `8`; equity avg `0.2702` n `65`; fx avg `0.0139` n `5`; index avg `0.0969` n `23`; metal avg `-0.1124` n `18`; unknown avg `0.1539` n `384`
- 24h: commodity avg `1.8283` n `12`; crypto_alt avg `-9.2329` n `228`; crypto_major avg `-1.4951` n `8`; equity avg `-2.2799` n `65`; fx avg `-0.1519` n `5`; index avg `-1.4776` n `23`; metal avg `-5.9443` n `18`; unknown avg `550.2981` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
