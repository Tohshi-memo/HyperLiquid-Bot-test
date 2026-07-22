# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T10:52:32.087815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0667` n `12`; crypto_alt avg `0.0462` n `230`; crypto_major avg `0.1125` n `8`; equity avg `-0.0013` n `98`; fx avg `-0.0073` n `6`; index avg `0.0031` n `25`; metal avg `-0.0066` n `20`; unknown avg `-0.0136` n `773`
- 1h: commodity avg `-0.1577` n `12`; crypto_alt avg `0.3063` n `230`; crypto_major avg `0.4145` n `8`; equity avg `0.2108` n `98`; fx avg `-0.0245` n `6`; index avg `0.056` n `25`; metal avg `0.0062` n `20`; unknown avg `0.038` n `773`
- 4h: commodity avg `0.1517` n `12`; crypto_alt avg `0.5849` n `230`; crypto_major avg `0.5262` n `8`; equity avg `0.1515` n `98`; fx avg `-0.0099` n `6`; index avg `0.0415` n `25`; metal avg `0.0343` n `20`; unknown avg `0.065` n `772`
- 24h: commodity avg `0.606` n `12`; crypto_alt avg `-0.4384` n `230`; crypto_major avg `-0.9869` n `8`; equity avg `0.6169` n `98`; fx avg `-0.0137` n `6`; index avg `-0.0003` n `25`; metal avg `0.3145` n `20`; unknown avg `0.0481` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1034`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0795`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0707`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0687`, n `666`, weak_sample_signal
