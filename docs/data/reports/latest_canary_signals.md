# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T17:53:27.134262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1824` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0176` n `12`; crypto_alt avg `0.0585` n `228`; crypto_major avg `0.0744` n `8`; equity avg `0.1018` n `66`; fx avg `-0.0007` n `5`; index avg `0.0488` n `23`; metal avg `-0.0298` n `18`; unknown avg `0.1165` n `384`
- 1h: commodity avg `0.0828` n `12`; crypto_alt avg `0.1917` n `228`; crypto_major avg `0.2569` n `8`; equity avg `-0.0063` n `66`; fx avg `-0.0333` n `5`; index avg `-0.0578` n `23`; metal avg `0.0018` n `18`; unknown avg `0.0112` n `384`
- 4h: commodity avg `1.615` n `12`; crypto_alt avg `-0.5009` n `228`; crypto_major avg `-0.5674` n `8`; equity avg `-1.4816` n `66`; fx avg `-0.0274` n `5`; index avg `-0.7527` n `23`; metal avg `-0.5891` n `18`; unknown avg `-0.0159` n `384`
- 24h: commodity avg `1.1369` n `12`; crypto_alt avg `-1.9744` n `228`; crypto_major avg `-1.6189` n `8`; equity avg `-0.838` n `66`; fx avg `0.0128` n `5`; index avg `-0.4832` n `23`; metal avg `0.5917` n `18`; unknown avg `-0.3205` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
