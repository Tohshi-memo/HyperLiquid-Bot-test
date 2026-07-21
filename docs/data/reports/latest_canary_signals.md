# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T23:22:29.379400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `0.0134` n `230`; crypto_major avg `-0.0142` n `8`; equity avg `0.1857` n `98`; fx avg `0.0045` n `6`; index avg `-0.0018` n `25`; metal avg `0.015` n `20`; unknown avg `-0.0302` n `771`
- 1h: commodity avg `0.0027` n `12`; crypto_alt avg `-0.2258` n `230`; crypto_major avg `-0.1579` n `8`; equity avg `0.0956` n `98`; fx avg `0.0026` n `6`; index avg `-0.0079` n `25`; metal avg `0.0167` n `20`; unknown avg `-0.1127` n `771`
- 4h: commodity avg `0.0304` n `12`; crypto_alt avg `-0.2381` n `230`; crypto_major avg `-0.2109` n `8`; equity avg `0.8669` n `98`; fx avg `-0.0111` n `6`; index avg `0.0177` n `25`; metal avg `-0.0201` n `20`; unknown avg `-0.2075` n `771`
- 24h: commodity avg `0.4762` n `12`; crypto_alt avg `0.5697` n `230`; crypto_major avg `0.4148` n `8`; equity avg `4.3758` n `98`; fx avg `0.0622` n `6`; index avg `0.6113` n `25`; metal avg `0.778` n `20`; unknown avg `0.131` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0899`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.051`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0485`, n `666`, weak_sample_signal
