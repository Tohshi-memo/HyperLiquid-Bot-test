# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T19:52:16.134823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.3274` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1714` n `12`; crypto_alt avg `0.4374` n `228`; crypto_major avg `0.6426` n `8`; equity avg `0.4549` n `66`; fx avg `0.0039` n `6`; index avg `0.2195` n `23`; metal avg `0.1222` n `18`; unknown avg `0.0343` n `383`
- 1h: commodity avg `-0.8855` n `12`; crypto_alt avg `1.6061` n `228`; crypto_major avg `1.4419` n `8`; equity avg `1.0462` n `66`; fx avg `0.0255` n `6`; index avg `0.5096` n `23`; metal avg `0.5369` n `18`; unknown avg `0.8513` n `383`
- 4h: commodity avg `-0.2808` n `12`; crypto_alt avg `1.1651` n `228`; crypto_major avg `1.3173` n `8`; equity avg `0.2894` n `66`; fx avg `-0.0241` n `6`; index avg `0.1293` n `23`; metal avg `0.4631` n `18`; unknown avg `0.1721` n `383`
- 24h: commodity avg `0.5301` n `12`; crypto_alt avg `-1.8296` n `228`; crypto_major avg `-2.0521` n `8`; equity avg `-0.8692` n `66`; fx avg `0.1635` n `6`; index avg `-0.3521` n `23`; metal avg `0.9396` n `18`; unknown avg `-0.6724` n `362`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
