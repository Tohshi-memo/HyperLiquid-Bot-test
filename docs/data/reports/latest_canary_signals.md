# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T11:41:03.077070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.0701` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.0477` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.0385` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-1.8317` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `0.6765` n `230`; crypto_major avg `0.5123` n `8`; equity avg `0.0401` n `121`; fx avg `0.0005` n `6`; index avg `0.0093` n `25`; metal avg `0.0233` n `20`; unknown avg `0.1199` n `794`
- 1h: commodity avg `-0.0046` n `12`; crypto_alt avg `0.2154` n `230`; crypto_major avg `-0.0389` n `8`; equity avg `-0.0275` n `121`; fx avg `0.0099` n `6`; index avg `0.0134` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.0446` n `794`
- 4h: commodity avg `-0.0248` n `12`; crypto_alt avg `-1.5291` n `230`; crypto_major avg `-2.0633` n `8`; equity avg `-0.2316` n `121`; fx avg `0.0365` n `6`; index avg `-0.0156` n `25`; metal avg `0.0068` n `20`; unknown avg `0.1078` n `794`
- 24h: commodity avg `0.1058` n `12`; crypto_alt avg `2.2073` n `230`; crypto_major avg `3.6834` n `8`; equity avg `-1.0556` n `121`; fx avg `0.0771` n `6`; index avg `-0.1476` n `25`; metal avg `-0.2294` n `20`; unknown avg `1.4528` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
