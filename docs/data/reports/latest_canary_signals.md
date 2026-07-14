# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T14:07:37.645135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3233` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.1351` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1387` n `12`; crypto_alt avg `-0.1449` n `230`; crypto_major avg `-0.1174` n `8`; equity avg `-0.3647` n `92`; fx avg `0.0072` n `6`; index avg `-0.0558` n `25`; metal avg `0.018` n `20`; unknown avg `19.2988` n `766`
- 1h: commodity avg `-0.1564` n `12`; crypto_alt avg `0.1463` n `230`; crypto_major avg `0.2251` n `8`; equity avg `-0.777` n `92`; fx avg `0.013` n `6`; index avg `-0.0393` n `25`; metal avg `0.1488` n `20`; unknown avg `12.9706` n `766`
- 4h: commodity avg `-0.3684` n `12`; crypto_alt avg `1.2749` n `230`; crypto_major avg `1.9549` n `8`; equity avg `-0.1802` n `92`; fx avg `0.0054` n `6`; index avg `0.1896` n `25`; metal avg `0.5207` n `20`; unknown avg `0.6153` n `766`
- 24h: commodity avg `1.2017` n `12`; crypto_alt avg `0.7412` n `230`; crypto_major avg `2.1493` n `8`; equity avg `0.1292` n `92`; fx avg `-0.0148` n `6`; index avg `0.1034` n `25`; metal avg `0.5469` n `20`; unknown avg `-0.0566` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
