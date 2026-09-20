# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T08:52:28.814732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0207` n `12`; crypto_alt avg `-0.2491` n `234`; crypto_major avg `-0.2061` n `8`; equity avg `-0.0408` n `140`; fx avg `-0.0001` n `6`; index avg `0.0002` n `26`; metal avg `-0.0118` n `20`; unknown avg `1.705` n `943`
- 1h: commodity avg `-0.0353` n `12`; crypto_alt avg `-0.2767` n `234`; crypto_major avg `-0.2406` n `8`; equity avg `-0.049` n `140`; fx avg `0.0027` n `6`; index avg `-0.0037` n `26`; metal avg `0.0015` n `20`; unknown avg `1.8015` n `935`
- 4h: commodity avg `0.0309` n `12`; crypto_alt avg `-0.869` n `234`; crypto_major avg `-0.3609` n `8`; equity avg `-0.0437` n `140`; fx avg `0.004` n `6`; index avg `-0.0154` n `26`; metal avg `0.0037` n `20`; unknown avg `9.3873` n `905`
- 24h: commodity avg `0.2655` n `12`; crypto_alt avg `-1.502` n `234`; crypto_major avg `-2.3204` n `8`; equity avg `-0.2902` n `140`; fx avg `-0.04` n `6`; index avg `-0.0649` n `26`; metal avg `0.0046` n `20`; unknown avg `0.6473` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
