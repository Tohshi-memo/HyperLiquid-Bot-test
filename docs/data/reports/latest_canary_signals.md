# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T00:37:24.621118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3631` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.331` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2828` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `0.1655` n `230`; crypto_major avg `-0.1773` n `8`; equity avg `-0.0035` n `121`; fx avg `0.0` n `6`; index avg `0.0011` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.0398` n `793`
- 1h: commodity avg `-0.0455` n `12`; crypto_alt avg `0.5841` n `230`; crypto_major avg `-0.3695` n `8`; equity avg `0.0393` n `121`; fx avg `0.002` n `6`; index avg `0.0045` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0542` n `793`
- 4h: commodity avg `-0.0266` n `12`; crypto_alt avg `2.4012` n `230`; crypto_major avg `2.3365` n `8`; equity avg `0.0537` n `121`; fx avg `0.0035` n `6`; index avg `0.0307` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.0963` n `793`
- 24h: commodity avg `0.1232` n `12`; crypto_alt avg `9.0074` n `230`; crypto_major avg `6.9351` n `8`; equity avg `0.779` n `121`; fx avg `-0.0027` n `6`; index avg `0.1031` n `25`; metal avg `0.5022` n `20`; unknown avg `1.2667` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2202`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
