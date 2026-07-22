# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T03:37:30.011346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `-0.0528` n `230`; crypto_major avg `-0.0704` n `8`; equity avg `0.0545` n `98`; fx avg `0.0107` n `6`; index avg `0.0189` n `25`; metal avg `-0.06` n `20`; unknown avg `-0.137` n `771`
- 1h: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.2279` n `230`; crypto_major avg `-0.238` n `8`; equity avg `-0.2319` n `98`; fx avg `0.0264` n `6`; index avg `-0.0406` n `25`; metal avg `0.0316` n `20`; unknown avg `-0.2449` n `771`
- 4h: commodity avg `0.0457` n `12`; crypto_alt avg `-0.1149` n `230`; crypto_major avg `-0.1502` n `8`; equity avg `-0.5534` n `98`; fx avg `0.0366` n `6`; index avg `-0.025` n `25`; metal avg `0.4473` n `20`; unknown avg `-0.221` n `771`
- 24h: commodity avg `0.5976` n `12`; crypto_alt avg `0.0922` n `230`; crypto_major avg `-0.1484` n `8`; equity avg `2.5027` n `98`; fx avg `0.0766` n `6`; index avg `0.3402` n `25`; metal avg `0.8816` n `20`; unknown avg `0.3183` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0946`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.059`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0536`, n `666`, weak_sample_signal
