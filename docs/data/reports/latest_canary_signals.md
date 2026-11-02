# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T17:52:32.215655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.636` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4278` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0571` n `13`; crypto_alt avg `-0.3409` n `239`; crypto_major avg `-0.2814` n `8`; equity avg `-0.445` n `156`; fx avg `-0.004` n `6`; index avg `-0.0578` n `27`; metal avg `-0.0458` n `20`; unknown avg `-0.0233` n `1259`
- 1h: commodity avg `-0.2046` n `13`; crypto_alt avg `-1.1897` n `239`; crypto_major avg `-1.0636` n `8`; equity avg `-0.8808` n `156`; fx avg `0.0011` n `6`; index avg `-0.0922` n `27`; metal avg `-0.1383` n `20`; unknown avg `0.6006` n `1253`
- 4h: commodity avg `-0.6216` n `13`; crypto_alt avg `-1.8656` n `239`; crypto_major avg `-1.5535` n `8`; equity avg `-2.2659` n `156`; fx avg `0.0115` n `6`; index avg `-0.1257` n `27`; metal avg `0.0825` n `20`; unknown avg `15.6505` n `1247`
- 24h: commodity avg `-1.3739` n `13`; crypto_alt avg `-3.2485` n `238`; crypto_major avg `-1.8587` n `8`; equity avg `-1.7082` n `156`; fx avg `0.2716` n `6`; index avg `0.1191` n `27`; metal avg `0.274` n `20`; unknown avg `7.6269` n `1073`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
