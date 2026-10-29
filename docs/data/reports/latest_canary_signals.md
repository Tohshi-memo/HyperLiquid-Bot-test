# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T04:07:36.816739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.222` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0581` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9827` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0107` n `13`; crypto_alt avg `-0.1739` n `238`; crypto_major avg `-0.1034` n `8`; equity avg `-0.056` n `155`; fx avg `0.0039` n `6`; index avg `-0.0076` n `27`; metal avg `-0.0186` n `20`; unknown avg `0.1675` n `1224`
- 1h: commodity avg `-0.0061` n `13`; crypto_alt avg `-0.5215` n `238`; crypto_major avg `-0.3578` n `8`; equity avg `-0.109` n `155`; fx avg `0.0084` n `6`; index avg `-0.0175` n `27`; metal avg `-0.0595` n `20`; unknown avg `-0.2393` n `1216`
- 4h: commodity avg `-0.021` n `13`; crypto_alt avg `-3.0686` n `238`; crypto_major avg `-2.243` n `8`; equity avg `-1.2712` n `155`; fx avg `-0.0775` n `6`; index avg `-0.1849` n `27`; metal avg `-0.2603` n `20`; unknown avg `3.1349` n `1208`
- 24h: commodity avg `-0.0745` n `13`; crypto_alt avg `-2.7919` n `238`; crypto_major avg `-1.976` n `8`; equity avg `-1.5151` n `154`; fx avg `-0.0152` n `6`; index avg `-0.1593` n `27`; metal avg `-0.26` n `20`; unknown avg `29.2336` n `978`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
