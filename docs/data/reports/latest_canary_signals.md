# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T01:37:26.241945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0349` n `11`; crypto_alt avg `-0.0205` n `230`; crypto_major avg `0.057` n `8`; equity avg `-0.324` n `87`; fx avg `-0.0098` n `5`; index avg `0.009` n `19`; metal avg `0.0596` n `16`; unknown avg `-0.0157` n `754`
- 1h: commodity avg `0.215` n `12`; crypto_alt avg `-0.1696` n `230`; crypto_major avg `-0.1672` n `8`; equity avg `-0.3328` n `98`; fx avg `0.0074` n `6`; index avg `-0.0088` n `25`; metal avg `0.3077` n `20`; unknown avg `-0.1487` n `771`
- 4h: commodity avg `0.2042` n `12`; crypto_alt avg `-0.1031` n `230`; crypto_major avg `0.1479` n `8`; equity avg `-0.1713` n `98`; fx avg `0.0089` n `6`; index avg `0.023` n `25`; metal avg `0.3914` n `20`; unknown avg `-0.2969` n `771`
- 24h: commodity avg `0.7111` n `12`; crypto_alt avg `0.6342` n `230`; crypto_major avg `0.542` n `8`; equity avg `3.7229` n `98`; fx avg `0.0146` n `6`; index avg `0.5078` n `25`; metal avg `1.0164` n `20`; unknown avg `0.3708` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0955`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0575`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0502`, n `666`, weak_sample_signal
