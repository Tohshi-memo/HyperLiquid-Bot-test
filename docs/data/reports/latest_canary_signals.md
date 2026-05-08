# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T19:22:16.468697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1014` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0271` n `12`; crypto_alt avg `0.0253` n `228`; crypto_major avg `0.0855` n `8`; equity avg `0.0474` n `65`; fx avg `0.006` n `5`; index avg `0.0418` n `23`; metal avg `-0.0244` n `18`; unknown avg `-0.2392` n `375`
- 1h: commodity avg `0.0191` n `12`; crypto_alt avg `0.0773` n `228`; crypto_major avg `0.1659` n `8`; equity avg `0.1464` n `65`; fx avg `0.0191` n `5`; index avg `-0.0778` n `23`; metal avg `-0.1702` n `18`; unknown avg `0.0213` n `375`
- 4h: commodity avg `-0.4337` n `12`; crypto_alt avg `1.9286` n `228`; crypto_major avg `1.6677` n `8`; equity avg `0.6724` n `65`; fx avg `0.0266` n `5`; index avg `0.4059` n `23`; metal avg `0.362` n `18`; unknown avg `-0.0021` n `375`
- 24h: commodity avg `-0.1914` n `12`; crypto_alt avg `3.4099` n `228`; crypto_major avg `1.6349` n `8`; equity avg `3.361` n `65`; fx avg `0.1893` n `5`; index avg `1.5818` n `23`; metal avg `0.9267` n `18`; unknown avg `0.7076` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1241`, n `665`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1203`, n `665`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0944`, n `665`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0934`, n `665`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0638`, n `665`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
