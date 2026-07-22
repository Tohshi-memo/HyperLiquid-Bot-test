# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T00:22:32.063062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `12`; crypto_alt avg `0.1328` n `230`; crypto_major avg `0.1536` n `8`; equity avg `-0.0295` n `98`; fx avg `-0.009` n `6`; index avg `-0.0143` n `25`; metal avg `0.038` n `20`; unknown avg `0.0801` n `771`
- 1h: commodity avg `0.0079` n `12`; crypto_alt avg `0.4932` n `230`; crypto_major avg `0.6573` n `8`; equity avg `0.2649` n `98`; fx avg `-0.0047` n `6`; index avg `0.0673` n `25`; metal avg `0.1017` n `20`; unknown avg `0.3795` n `771`
- 4h: commodity avg `0.0305` n `12`; crypto_alt avg `0.2807` n `230`; crypto_major avg `0.4913` n `8`; equity avg `0.6052` n `98`; fx avg `-0.0261` n `6`; index avg `0.085` n `25`; metal avg `0.112` n `20`; unknown avg `0.0546` n `771`
- 24h: commodity avg `0.473` n `12`; crypto_alt avg `0.9672` n `230`; crypto_major avg `0.9803` n `8`; equity avg `4.8192` n `98`; fx avg `0.0231` n `6`; index avg `0.774` n `25`; metal avg `0.8428` n `20`; unknown avg `0.4431` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0875`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0521`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0483`, n `666`, weak_sample_signal
