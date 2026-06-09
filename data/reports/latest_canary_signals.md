# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T01:22:26.619078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7578` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7518` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5766` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0317` n `12`; crypto_alt avg `0.5524` n `228`; crypto_major avg `0.367` n `8`; equity avg `0.2014` n `74`; fx avg `0.0172` n `6`; index avg `0.1617` n `23`; metal avg `0.0967` n `18`; unknown avg `0.0582` n `517`
- 1h: commodity avg `-0.0307` n `12`; crypto_alt avg `-0.6249` n `228`; crypto_major avg `-0.7088` n `8`; equity avg `0.0068` n `74`; fx avg `-0.0976` n `6`; index avg `0.1329` n `23`; metal avg `0.2193` n `18`; unknown avg `0.0079` n `517`
- 4h: commodity avg `-0.2563` n `12`; crypto_alt avg `-2.249` n `228`; crypto_major avg `-1.9984` n `8`; equity avg `-0.4218` n `74`; fx avg `-0.0636` n `6`; index avg `-0.2406` n `23`; metal avg `-0.2466` n `18`; unknown avg `-0.5627` n `517`
- 24h: commodity avg `-1.0016` n `12`; crypto_alt avg `-0.0507` n `228`; crypto_major avg `0.2193` n `8`; equity avg `1.3182` n `74`; fx avg `-0.3005` n `6`; index avg `0.657` n `23`; metal avg `0.219` n `18`; unknown avg `-3.0444` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
