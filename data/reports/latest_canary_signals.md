# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T23:52:30.103528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9461` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2545` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0303` n `13`; crypto_alt avg `0.1703` n `237`; crypto_major avg `0.0103` n `8`; equity avg `0.1747` n `151`; fx avg `0.0062` n `6`; index avg `0.0381` n `26`; metal avg `0.0261` n `20`; unknown avg `0.1813` n `1194`
- 1h: commodity avg `-0.0739` n `13`; crypto_alt avg `0.6666` n `237`; crypto_major avg `0.3234` n `8`; equity avg `0.2452` n `151`; fx avg `0.0019` n `6`; index avg `0.0246` n `26`; metal avg `0.0436` n `20`; unknown avg `2.67` n `1192`
- 4h: commodity avg `-0.4241` n `13`; crypto_alt avg `3.135` n `237`; crypto_major avg `2.522` n `8`; equity avg `1.8011` n `151`; fx avg `0.0071` n `6`; index avg `0.3428` n `26`; metal avg `0.2675` n `20`; unknown avg `15.1263` n `1090`
- 24h: commodity avg `-0.3578` n `13`; crypto_alt avg `-1.3652` n `236`; crypto_major avg `0.6507` n `8`; equity avg `1.1728` n `151`; fx avg `-0.0164` n `6`; index avg `0.2631` n `26`; metal avg `0.233` n `20`; unknown avg `6.5658` n `961`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2008`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1363`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0905`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.087`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0697`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0661`, n `666`, weak_sample_signal
