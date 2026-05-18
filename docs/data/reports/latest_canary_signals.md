# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T22:52:17.144216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.261` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `-0.154` n `228`; crypto_major avg `-0.173` n `8`; equity avg `-0.0176` n `66`; fx avg `-0.0004` n `6`; index avg `-0.0115` n `23`; metal avg `-0.0381` n `18`; unknown avg `-0.1708` n `383`
- 1h: commodity avg `-0.0329` n `12`; crypto_alt avg `-0.0608` n `228`; crypto_major avg `-0.2459` n `8`; equity avg `0.1261` n `66`; fx avg `-0.0042` n `6`; index avg `-0.0325` n `23`; metal avg `0.2609` n `18`; unknown avg `-0.4601` n `383`
- 4h: commodity avg `-0.6424` n `12`; crypto_alt avg `2.0098` n `228`; crypto_major avg `1.6186` n `8`; equity avg `1.3832` n `66`; fx avg `0.0168` n `6`; index avg `0.7249` n `23`; metal avg `1.001` n `18`; unknown avg `0.6611` n `383`
- 24h: commodity avg `0.7828` n `12`; crypto_alt avg `-0.7011` n `228`; crypto_major avg `-1.0967` n `8`; equity avg `-0.9977` n `66`; fx avg `0.1706` n `6`; index avg `-0.2232` n `23`; metal avg `0.6592` n `18`; unknown avg `-0.1023` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
