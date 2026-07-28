# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T00:22:31.426904+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8012` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7181` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.079` n `12`; crypto_alt avg `-0.017` n `230`; crypto_major avg `-0.068` n `8`; equity avg `-0.3763` n `102`; fx avg `0.0125` n `6`; index avg `-0.108` n `25`; metal avg `-0.0221` n `20`; unknown avg `0.159` n `774`
- 1h: commodity avg `-0.1196` n `12`; crypto_alt avg `-0.3211` n `230`; crypto_major avg `-0.3763` n `8`; equity avg `-0.4743` n `102`; fx avg `0.0757` n `6`; index avg `-0.1831` n `25`; metal avg `-0.0895` n `20`; unknown avg `-0.0416` n `774`
- 4h: commodity avg `-0.0984` n `12`; crypto_alt avg `-1.9885` n `230`; crypto_major avg `-1.9414` n `8`; equity avg `-0.9557` n `102`; fx avg `0.0636` n `6`; index avg `-0.2233` n `25`; metal avg `-0.1402` n `20`; unknown avg `1.2776` n `774`
- 24h: commodity avg `-0.6855` n `12`; crypto_alt avg `-3.6651` n `230`; crypto_major avg `-2.9965` n `8`; equity avg `-2.2618` n `102`; fx avg `0.0059` n `6`; index avg `-0.6188` n `25`; metal avg `-0.2125` n `20`; unknown avg `1161.8105` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.3522`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.3047`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1938`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
