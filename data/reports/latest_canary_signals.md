# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T21:37:30.901439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `13`; crypto_alt avg `-0.0957` n `236`; crypto_major avg `-0.0816` n `8`; equity avg `-0.0098` n `151`; fx avg `-0.0029` n `6`; index avg `0.0022` n `26`; metal avg `0.0118` n `20`; unknown avg `-0.0302` n `1193`
- 1h: commodity avg `0.0612` n `13`; crypto_alt avg `0.2192` n `236`; crypto_major avg `0.2456` n `8`; equity avg `-0.0291` n `151`; fx avg `-0.0009` n `6`; index avg `0.0072` n `26`; metal avg `0.0119` n `20`; unknown avg `3.333` n `1185`
- 4h: commodity avg `-0.0554` n `13`; crypto_alt avg `0.2661` n `236`; crypto_major avg `0.2727` n `8`; equity avg `-0.6962` n `151`; fx avg `0.0073` n `6`; index avg `-0.1242` n `26`; metal avg `0.0222` n `20`; unknown avg `2.5369` n `1109`
- 24h: commodity avg `0.4345` n `13`; crypto_alt avg `-1.646` n `236`; crypto_major avg `-1.4779` n `8`; equity avg `-3.7719` n `151`; fx avg `0.0285` n `6`; index avg `-0.6237` n `26`; metal avg `-0.0894` n `20`; unknown avg `0.2708` n `896`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1614`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1135`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.109`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0905`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.077`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0723`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.069`, n `666`, weak_sample_signal
