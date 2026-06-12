# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T10:37:25.582339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0886` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.2217` n `12`; crypto_alt avg `-0.105` n `228`; crypto_major avg `-0.0919` n `8`; equity avg `-0.0841` n `74`; fx avg `0.0074` n `6`; index avg `-0.0845` n `23`; metal avg `-0.0073` n `18`; unknown avg `0.0399` n `643`
- 1h: commodity avg `0.2805` n `12`; crypto_alt avg `-0.1943` n `228`; crypto_major avg `-0.4275` n `8`; equity avg `-0.2837` n `74`; fx avg `0.0324` n `6`; index avg `-0.1981` n `23`; metal avg `-0.2869` n `18`; unknown avg `0.5698` n `643`
- 4h: commodity avg `-0.6779` n `12`; crypto_alt avg `1.7752` n `228`; crypto_major avg `1.4107` n `8`; equity avg `0.6887` n `74`; fx avg `0.0028` n `6`; index avg `0.2916` n `23`; metal avg `0.5863` n `18`; unknown avg `0.7795` n `531`
- 24h: commodity avg `-2.059` n `12`; crypto_alt avg `1.9661` n `228`; crypto_major avg `1.8165` n `8`; equity avg `2.6001` n `74`; fx avg `0.0473` n `6`; index avg `1.4481` n `23`; metal avg `3.182` n `18`; unknown avg `1.5201` n `514`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
