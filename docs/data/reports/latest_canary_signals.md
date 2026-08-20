# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T15:52:26.408610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.1982` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.0049` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `1.6992` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0154` n `12`; crypto_alt avg `0.2036` n `230`; crypto_major avg `0.5724` n `8`; equity avg `0.0884` n `121`; fx avg `-0.0048` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0226` n `20`; unknown avg `-0.0596` n `792`
- 1h: commodity avg `0.1062` n `12`; crypto_alt avg `0.9988` n `230`; crypto_major avg `1.4188` n `8`; equity avg `-0.2804` n `121`; fx avg `0.0106` n `6`; index avg `-0.0579` n `25`; metal avg `0.1265` n `20`; unknown avg `0.6663` n `792`
- 4h: commodity avg `-0.1771` n `12`; crypto_alt avg `1.0043` n `230`; crypto_major avg `1.8278` n `8`; equity avg `-0.3704` n `121`; fx avg `-0.0163` n `6`; index avg `0.006` n `25`; metal avg `0.4195` n `20`; unknown avg `-0.1428` n `792`
- 24h: commodity avg `0.0515` n `12`; crypto_alt avg `6.314` n `230`; crypto_major avg `9.6631` n `8`; equity avg `-0.5138` n `121`; fx avg `0.1712` n `6`; index avg `-0.0563` n `25`; metal avg `0.339` n `20`; unknown avg `2.2389` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
