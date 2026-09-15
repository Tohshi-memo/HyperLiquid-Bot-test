# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T22:07:30.470713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.5545` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.535` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.4651` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.1666` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.239` n `234`; crypto_major avg `-0.0709` n `8`; equity avg `0.0022` n `137`; fx avg `0.0069` n `6`; index avg `0.0003` n `27`; metal avg `0.0125` n `20`; unknown avg `0.3121` n `893`
- 1h: commodity avg `-0.0412` n `12`; crypto_alt avg `-0.6752` n `234`; crypto_major avg `-0.3879` n `8`; equity avg `-0.1221` n `137`; fx avg `0.0126` n `6`; index avg `-0.0086` n `27`; metal avg `0.008` n `20`; unknown avg `4.4652` n `877`
- 4h: commodity avg `-0.0593` n `12`; crypto_alt avg `-2.5409` n `234`; crypto_major avg `-2.5244` n `8`; equity avg `-0.3578` n `137`; fx avg `0.0116` n `6`; index avg `0.0106` n `27`; metal avg `0.0301` n `20`; unknown avg `1.1512` n `853`
- 24h: commodity avg `0.453` n `12`; crypto_alt avg `-4.6552` n `234`; crypto_major avg `-4.9841` n `8`; equity avg `-1.3018` n `137`; fx avg `0.215` n `6`; index avg `-0.066` n `27`; metal avg `0.169` n `20`; unknown avg `1.9801` n `802`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
