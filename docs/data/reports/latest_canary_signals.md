# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T03:37:29.121254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `13`; crypto_alt avg `0.4212` n `236`; crypto_major avg `0.1638` n `8`; equity avg `0.0762` n `151`; fx avg `-0.0005` n `6`; index avg `0.0039` n `26`; metal avg `0.0042` n `20`; unknown avg `0.1702` n `1193`
- 1h: commodity avg `-0.0033` n `13`; crypto_alt avg `0.6065` n `236`; crypto_major avg `0.4142` n `8`; equity avg `0.1719` n `151`; fx avg `-0.0008` n `6`; index avg `0.0163` n `26`; metal avg `0.013` n `20`; unknown avg `1.2276` n `1191`
- 4h: commodity avg `0.0969` n `13`; crypto_alt avg `0.2197` n `236`; crypto_major avg `-0.0153` n `8`; equity avg `0.4449` n `151`; fx avg `0.0026` n `6`; index avg `0.0424` n `26`; metal avg `0.0178` n `20`; unknown avg `0.1982` n `1183`
- 24h: commodity avg `0.6762` n `13`; crypto_alt avg `-0.1232` n `236`; crypto_major avg `-0.4642` n `8`; equity avg `-3.61` n `151`; fx avg `-0.0156` n `6`; index avg `-0.5858` n `26`; metal avg `-0.1588` n `20`; unknown avg `40.3547` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1716`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.118`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0934`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0763`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0719`, n `666`, weak_sample_signal
