# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T09:22:27.047757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `13`; crypto_alt avg `-0.073` n `236`; crypto_major avg `-0.0204` n `8`; equity avg `-0.0105` n `151`; fx avg `0.0026` n `6`; index avg `0.0078` n `26`; metal avg `-0.0056` n `20`; unknown avg `0.161` n `1193`
- 1h: commodity avg `0.0553` n `13`; crypto_alt avg `-0.155` n `236`; crypto_major avg `-0.1037` n `8`; equity avg `0.0114` n `151`; fx avg `-0.0218` n `6`; index avg `0.0054` n `26`; metal avg `0.0029` n `20`; unknown avg `0.0168` n `1191`
- 4h: commodity avg `-0.1778` n `13`; crypto_alt avg `-0.5478` n `236`; crypto_major avg `-0.0167` n `8`; equity avg `-0.017` n `151`; fx avg `-0.0153` n `6`; index avg `0.0134` n `26`; metal avg `0.0011` n `20`; unknown avg `0.0708` n `1157`
- 24h: commodity avg `0.5329` n `13`; crypto_alt avg `-2.1698` n `236`; crypto_major avg `-1.3881` n `8`; equity avg `-3.8138` n `151`; fx avg `0.0049` n `6`; index avg `-0.5955` n `26`; metal avg `-0.265` n `20`; unknown avg `8.8526` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1801`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1477`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1197`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0781`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
