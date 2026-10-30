# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T00:22:26.897962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.5425` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.4851` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-4.4593` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.9429` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `-2.3202` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.2916` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.2695` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-2.1597` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0031` n `13`; crypto_alt avg `-2.3624` n `238`; crypto_major avg `-1.4803` n `8`; equity avg `-0.2367` n `156`; fx avg `-0.0102` n `6`; index avg `-0.006` n `27`; metal avg `0.0187` n `20`; unknown avg `7.433` n `1258`
- 1h: commodity avg `0.0124` n `13`; crypto_alt avg `-3.2029` n `238`; crypto_major avg `-2.3078` n `8`; equity avg `-0.1481` n `156`; fx avg `-0.017` n `6`; index avg `-0.0162` n `27`; metal avg `-0.0383` n `20`; unknown avg `8.7769` n `1238`
- 4h: commodity avg `-0.0485` n `13`; crypto_alt avg `-6.6654` n `238`; crypto_major avg `-4.591` n `8`; equity avg `-1.6481` n `156`; fx avg `-0.0026` n `6`; index avg `-0.1059` n `27`; metal avg `-0.1317` n `20`; unknown avg `179.1689` n `1218`
- 24h: commodity avg `-0.2728` n `13`; crypto_alt avg `-8.6686` n `238`; crypto_major avg `-4.3089` n `8`; equity avg `-3.8361` n `155`; fx avg `0.117` n `6`; index avg `-0.3582` n `27`; metal avg `-0.5775` n `20`; unknown avg `34.7958` n `988`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
