# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T00:07:25.219740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0815` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2735` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0403` n `13`; crypto_alt avg `0.0845` n `237`; crypto_major avg `0.0848` n `8`; equity avg `0.5984` n `151`; fx avg `0.0201` n `6`; index avg `0.1445` n `26`; metal avg `0.0372` n `20`; unknown avg `-0.1095` n `1184`
- 1h: commodity avg `-0.1449` n `13`; crypto_alt avg `0.7436` n `237`; crypto_major avg `0.4967` n `8`; equity avg `1.0002` n `151`; fx avg `0.0278` n `6`; index avg `0.2191` n `26`; metal avg `0.0651` n `20`; unknown avg `1.9288` n `1184`
- 4h: commodity avg `-0.486` n `13`; crypto_alt avg `3.2561` n `237`; crypto_major avg `2.5955` n `8`; equity avg `2.4393` n `151`; fx avg `0.0484` n `6`; index avg `0.4889` n `26`; metal avg `0.322` n `20`; unknown avg `11.369` n `1096`
- 24h: commodity avg `-0.4011` n `13`; crypto_alt avg `-1.2496` n `236`; crypto_major avg `0.771` n `8`; equity avg `1.9379` n `151`; fx avg `0.0026` n `6`; index avg `0.4211` n `26`; metal avg `0.2811` n `20`; unknown avg `2.1674` n `959`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2002`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.136`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0895`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0788`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0735`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0656`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
