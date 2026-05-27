# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T16:37:21.010455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0217` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0578` n `12`; crypto_alt avg `-0.204` n `228`; crypto_major avg `-0.1412` n `8`; equity avg `0.0827` n `67`; fx avg `-0.0014` n `6`; index avg `0.0413` n `23`; metal avg `0.0944` n `18`; unknown avg `-0.0845` n `418`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.8607` n `228`; crypto_major avg `-0.7676` n `8`; equity avg `0.226` n `67`; fx avg `0.0018` n `6`; index avg `0.1902` n `23`; metal avg `0.1651` n `18`; unknown avg `-0.47` n `418`
- 4h: commodity avg `1.0334` n `12`; crypto_alt avg `-0.3676` n `228`; crypto_major avg `-0.9883` n `8`; equity avg `-0.9973` n `67`; fx avg `-0.0524` n `6`; index avg `-0.8626` n `23`; metal avg `-0.0124` n `18`; unknown avg `-0.152` n `418`
- 24h: commodity avg `-1.1311` n `12`; crypto_alt avg `-1.2324` n `228`; crypto_major avg `-1.3478` n `8`; equity avg `-0.4372` n `67`; fx avg `-0.0713` n `6`; index avg `-0.4909` n `23`; metal avg `-0.9703` n `18`; unknown avg `-0.8053` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
