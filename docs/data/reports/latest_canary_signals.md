# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T16:07:20.754760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1255` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.1698` n `12`; crypto_alt avg `-0.0114` n `228`; crypto_major avg `0.016` n `8`; equity avg `-0.0138` n `66`; fx avg `-0.0037` n `5`; index avg `-0.0089` n `23`; metal avg `0.0808` n `18`; unknown avg `-0.2472` n `384`
- 1h: commodity avg `0.1434` n `12`; crypto_alt avg `0.3574` n `228`; crypto_major avg `0.2714` n `8`; equity avg `-0.2136` n `66`; fx avg `-0.0042` n `5`; index avg `-0.1267` n `23`; metal avg `0.2872` n `18`; unknown avg `-0.6048` n `384`
- 4h: commodity avg `0.7702` n `12`; crypto_alt avg `-0.9618` n `228`; crypto_major avg `-1.3553` n `8`; equity avg `-1.6948` n `66`; fx avg `-0.0141` n `5`; index avg `-0.506` n `23`; metal avg `-0.0122` n `18`; unknown avg `0.128` n `383`
- 24h: commodity avg `1.0246` n `12`; crypto_alt avg `-2.8837` n `228`; crypto_major avg `-2.2371` n `8`; equity avg `-0.8758` n `66`; fx avg `0.0515` n `5`; index avg `-0.4496` n `23`; metal avg `0.425` n `18`; unknown avg `-0.5507` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
