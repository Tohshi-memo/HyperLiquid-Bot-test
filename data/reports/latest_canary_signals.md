# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T16:07:27.438319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.2538` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.1826` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0015` n `13`; crypto_alt avg `0.3681` n `236`; crypto_major avg `0.0944` n `8`; equity avg `0.0353` n `151`; fx avg `-0.0148` n `6`; index avg `0.0123` n `26`; metal avg `-0.0273` n `20`; unknown avg `-0.0188` n `1128`
- 1h: commodity avg `0.0502` n `13`; crypto_alt avg `1.1256` n `236`; crypto_major avg `0.6779` n `8`; equity avg `0.3326` n `151`; fx avg `0.0053` n `6`; index avg `0.0128` n `26`; metal avg `-0.0065` n `20`; unknown avg `-0.1026` n `1128`
- 4h: commodity avg `0.1231` n `13`; crypto_alt avg `3.8025` n `236`; crypto_major avg `2.3057` n `8`; equity avg `1.495` n `151`; fx avg `-0.0143` n `6`; index avg `0.2475` n `26`; metal avg `0.0519` n `20`; unknown avg `3.2679` n `1082`
- 24h: commodity avg `-0.0046` n `13`; crypto_alt avg `1.154` n `236`; crypto_major avg `0.5997` n `8`; equity avg `-2.0035` n `151`; fx avg `0.181` n `6`; index avg `-0.3343` n `26`; metal avg `0.3672` n `20`; unknown avg `0.2197` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1109`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.095`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0872`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0812`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0782`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0646`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0631`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
