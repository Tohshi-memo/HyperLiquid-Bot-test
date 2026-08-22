# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T04:45:18.428501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `5.7753` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `5.7418` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `5.6525` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `1.7113` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.6844` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0311` n `12`; crypto_alt avg `0.1513` n `230`; crypto_major avg `0.2718` n `8`; equity avg `-0.018` n `121`; fx avg `-0.002` n `6`; index avg `0.0018` n `25`; metal avg `-0.0056` n `20`; unknown avg `0.3791` n `794`
- 1h: commodity avg `0.052` n `12`; crypto_alt avg `1.018` n `230`; crypto_major avg `1.6532` n `8`; equity avg `-0.0581` n `121`; fx avg `0.0046` n `6`; index avg `-0.0265` n `25`; metal avg `-0.0312` n `20`; unknown avg `0.7465` n `794`
- 4h: commodity avg `0.0727` n `12`; crypto_alt avg `4.5903` n `230`; crypto_major avg `5.7252` n `8`; equity avg `-0.0166` n `121`; fx avg `0.0385` n `6`; index avg `-0.0165` n `25`; metal avg `-0.0501` n `20`; unknown avg `1.1072` n `793`
- 24h: commodity avg `0.1676` n `12`; crypto_alt avg `12.7809` n `230`; crypto_major avg `11.6892` n `8`; equity avg `0.2721` n `121`; fx avg `0.0711` n `6`; index avg `-0.0258` n `25`; metal avg `0.1492` n `20`; unknown avg `2.2981` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
