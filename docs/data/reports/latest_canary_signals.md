# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T05:37:27.165422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-4.3173` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `4.2202` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-4.1551` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-3.7944` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0347` n `12`; crypto_alt avg `1.3855` n `230`; crypto_major avg `1.6762` n `8`; equity avg `0.2257` n `121`; fx avg `0.0081` n `6`; index avg `0.0177` n `25`; metal avg `0.0511` n `20`; unknown avg `0.1817` n `794`
- 1h: commodity avg `0.0783` n `12`; crypto_alt avg `-5.0149` n `230`; crypto_major avg `-4.239` n `8`; equity avg `-0.4446` n `121`; fx avg `-0.0` n `6`; index avg `-0.0188` n `25`; metal avg `-0.0839` n `20`; unknown avg `1.0953` n `794`
- 4h: commodity avg `0.1023` n `12`; crypto_alt avg `-1.3682` n `230`; crypto_major avg `-0.1068` n `8`; equity avg `-0.4103` n `121`; fx avg `0.0341` n `6`; index avg `-0.0313` n `25`; metal avg `-0.1142` n `20`; unknown avg `0.2277` n `793`
- 24h: commodity avg `0.2148` n `12`; crypto_alt avg `6.474` n `230`; crypto_major avg `6.2678` n `8`; equity avg `-0.2755` n `121`; fx avg `0.0685` n `6`; index avg `-0.0511` n `25`; metal avg `0.0889` n `20`; unknown avg `1.9697` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
