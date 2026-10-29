# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T21:22:27.590908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.1618` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.9598` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.8197` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.4386` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0154` n `13`; crypto_alt avg `0.4349` n `238`; crypto_major avg `0.83` n `8`; equity avg `-0.3416` n `156`; fx avg `-0.0048` n `6`; index avg `-0.0221` n `27`; metal avg `0.0017` n `20`; unknown avg `11.2064` n `1260`
- 1h: commodity avg `-0.0491` n `13`; crypto_alt avg `-2.4571` n `238`; crypto_major avg `-1.4965` n `8`; equity avg `-1.1034` n `156`; fx avg `0.0001` n `6`; index avg `-0.0579` n `27`; metal avg `-0.0587` n `20`; unknown avg `174.3172` n `1232`
- 4h: commodity avg `0.1453` n `13`; crypto_alt avg `-4.651` n `238`; crypto_major avg `-3.0165` n `8`; equity avg `-2.6516` n `156`; fx avg `0.0059` n `6`; index avg `-0.1968` n `27`; metal avg `-0.0567` n `20`; unknown avg `29.7155` n `1162`
- 24h: commodity avg `-0.221` n `13`; crypto_alt avg `-5.2458` n `238`; crypto_major avg `-1.6566` n `8`; equity avg `-3.1507` n `155`; fx avg `0.0521` n `6`; index avg `-0.2658` n `27`; metal avg `-0.6152` n `20`; unknown avg `30.6137` n `976`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
