# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T18:52:27.122049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.7825` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.4145` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `3.3672` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0639` n `12`; crypto_alt avg `0.1056` n `230`; crypto_major avg `0.1354` n `8`; equity avg `0.1012` n `121`; fx avg `0.0044` n `6`; index avg `0.0029` n `25`; metal avg `0.0884` n `20`; unknown avg `0.1222` n `792`
- 1h: commodity avg `-0.2783` n `12`; crypto_alt avg `0.0895` n `230`; crypto_major avg `0.2537` n `8`; equity avg `-0.139` n `121`; fx avg `-0.0064` n `6`; index avg `0.009` n `25`; metal avg `0.0699` n `20`; unknown avg `1.0442` n `792`
- 4h: commodity avg `-0.2589` n `12`; crypto_alt avg `1.9081` n `230`; crypto_major avg `3.5236` n `8`; equity avg `0.1091` n `121`; fx avg `0.0206` n `6`; index avg `-0.027` n `25`; metal avg `0.1564` n `20`; unknown avg `0.1037` n `792`
- 24h: commodity avg `-0.0092` n `12`; crypto_alt avg `2.8163` n `230`; crypto_major avg `4.9301` n `8`; equity avg `-0.4787` n `120`; fx avg `-0.1913` n `6`; index avg `0.0023` n `25`; metal avg `0.8899` n `20`; unknown avg `0.4189` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
