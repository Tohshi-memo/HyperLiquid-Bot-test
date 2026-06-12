# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T15:22:30.576777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.4663` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.3333` n `12`; crypto_alt avg `-0.2255` n `228`; crypto_major avg `-0.1617` n `8`; equity avg `0.1387` n `74`; fx avg `-0.0009` n `6`; index avg `0.1246` n `23`; metal avg `0.3219` n `18`; unknown avg `0.0014` n `643`
- 1h: commodity avg `-1.0164` n `12`; crypto_alt avg `1.0133` n `228`; crypto_major avg `1.4499` n `8`; equity avg `0.6539` n `74`; fx avg `-0.0042` n `6`; index avg `0.3579` n `23`; metal avg `0.7275` n `18`; unknown avg `0.092` n `643`
- 4h: commodity avg `0.4549` n `12`; crypto_alt avg `0.3427` n `228`; crypto_major avg `1.207` n `8`; equity avg `-0.0745` n `74`; fx avg `-0.0288` n `6`; index avg `0.4014` n `23`; metal avg `0.0182` n `18`; unknown avg `14.7289` n `643`
- 24h: commodity avg `-2.1316` n `12`; crypto_alt avg `2.2782` n `228`; crypto_major avg `3.2011` n `8`; equity avg `2.9071` n `74`; fx avg `0.0596` n `6`; index avg `2.0217` n `23`; metal avg `2.9109` n `18`; unknown avg `21.6727` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
