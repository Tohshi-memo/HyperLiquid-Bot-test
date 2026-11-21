# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T08:07:35.680783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9884` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.7849` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9837` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0297` n `13`; crypto_alt avg `-0.1311` n `239`; crypto_major avg `-0.3701` n `8`; equity avg `-0.0283` n `166`; fx avg `0.0049` n `6`; index avg `-0.0058` n `27`; metal avg `0.0014` n `20`; unknown avg `0.0746` n `1234`
- 1h: commodity avg `-0.0464` n `13`; crypto_alt avg `-0.7884` n `239`; crypto_major avg `-1.0099` n `8`; equity avg `-0.2582` n `166`; fx avg `0.0042` n `6`; index avg `-0.026` n `27`; metal avg `-0.0553` n `20`; unknown avg `161.4712` n `1238`
- 4h: commodity avg `-0.0175` n `13`; crypto_alt avg `2.2478` n `239`; crypto_major avg `2.9709` n `8`; equity avg `0.9872` n `166`; fx avg `-0.0831` n `6`; index avg `0.1239` n `27`; metal avg `0.186` n `20`; unknown avg `0.0135` n `1202`
- 24h: commodity avg `0.4128` n `13`; crypto_alt avg `-6.1309` n `239`; crypto_major avg `-7.2234` n `8`; equity avg `-5.2081` n `166`; fx avg `-0.1368` n `6`; index avg `-0.5821` n `27`; metal avg `-0.3949` n `20`; unknown avg `15.7813` n `1137`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
