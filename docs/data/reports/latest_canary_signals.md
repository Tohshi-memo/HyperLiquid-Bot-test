# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T04:37:29.886120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `5.4794` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `5.4441` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `5.4213` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `0.6815` n `230`; crypto_major avg `1.4494` n `8`; equity avg `0.014` n `121`; fx avg `0.0001` n `6`; index avg `0.002` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.1296` n `794`
- 1h: commodity avg `0.021` n `12`; crypto_alt avg `1.1402` n `230`; crypto_major avg `1.357` n `8`; equity avg `-0.0528` n `121`; fx avg `0.0152` n `6`; index avg `-0.0218` n `25`; metal avg `-0.0336` n `20`; unknown avg `0.429` n `794`
- 4h: commodity avg `0.009` n `12`; crypto_alt avg `4.482` n `230`; crypto_major avg `5.4303` n `8`; equity avg `-0.0138` n `121`; fx avg `0.0395` n `6`; index avg `-0.0194` n `25`; metal avg `-0.0491` n `20`; unknown avg `0.7081` n `793`
- 24h: commodity avg `0.1069` n `12`; crypto_alt avg `12.7839` n `230`; crypto_major avg `11.5485` n `8`; equity avg `0.4242` n `121`; fx avg `0.0631` n `6`; index avg `0.0171` n `25`; metal avg `0.15` n `20`; unknown avg `2.3122` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
