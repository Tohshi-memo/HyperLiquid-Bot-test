# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T05:14:02.943366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.9007` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.7969` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.6128` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-2.1069` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `-5.783` n `230`; crypto_major avg `-4.4963` n `8`; equity avg `-0.7523` n `121`; fx avg `-0.0015` n `6`; index avg `-0.0894` n `25`; metal avg `-0.2325` n `20`; unknown avg `6.4292` n `794`
- 1h: commodity avg `0.0238` n `12`; crypto_alt avg `-4.5213` n `230`; crypto_major avg `-2.8769` n `8`; equity avg `-0.77` n `121`; fx avg `0.0115` n `6`; index avg `-0.08` n `25`; metal avg `-0.2641` n `20`; unknown avg `3.443` n `794`
- 4h: commodity avg `0.058` n `12`; crypto_alt avg `-1.7855` n `230`; crypto_major avg `0.0004` n `8`; equity avg `-0.7337` n `121`; fx avg `0.0305` n `6`; index avg `-0.0933` n `25`; metal avg `-0.2793` n `20`; unknown avg `0.7261` n `793`
- 24h: commodity avg `0.2013` n `12`; crypto_alt avg `6.336` n `230`; crypto_major avg `6.2414` n `8`; equity avg `-0.5399` n `121`; fx avg `0.0647` n `6`; index avg `-0.1049` n `25`; metal avg `-0.0461` n `20`; unknown avg `1.2541` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
