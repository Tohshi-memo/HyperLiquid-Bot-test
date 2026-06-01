# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T05:37:18.213405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0977` n `12`; crypto_alt avg `-0.564` n `228`; crypto_major avg `-0.4205` n `8`; equity avg `-0.1372` n `69`; fx avg `0.0183` n `6`; index avg `-0.2282` n `23`; metal avg `-0.1399` n `18`; unknown avg `-0.3619` n `422`
- 1h: commodity avg `0.0543` n `12`; crypto_alt avg `-0.6495` n `228`; crypto_major avg `-0.1764` n `8`; equity avg `-0.084` n `69`; fx avg `0.0072` n `6`; index avg `-0.3437` n `23`; metal avg `0.0767` n `18`; unknown avg `-0.5118` n `422`
- 4h: commodity avg `0.031` n `12`; crypto_alt avg `-0.3845` n `228`; crypto_major avg `-0.4119` n `8`; equity avg `0.0959` n `69`; fx avg `0.0046` n `6`; index avg `-0.0178` n `23`; metal avg `0.0654` n `18`; unknown avg `-0.6258` n `421`
- 24h: commodity avg `1.0352` n `12`; crypto_alt avg `-0.2491` n `228`; crypto_major avg `-1.0605` n `8`; equity avg `0.3606` n `69`; fx avg `0.0345` n `6`; index avg `0.2756` n `23`; metal avg `0.2387` n `18`; unknown avg `1.3068` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2871`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2247`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
