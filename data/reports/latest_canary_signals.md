# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T03:22:26.769917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8574` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.5285` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2195` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0072` n `13`; crypto_alt avg `-0.2691` n `239`; crypto_major avg `-0.2598` n `8`; equity avg `-0.1441` n `158`; fx avg `0.0043` n `6`; index avg `-0.0257` n `27`; metal avg `0.0167` n `20`; unknown avg `0.3111` n `1260`
- 1h: commodity avg `0.1726` n `13`; crypto_alt avg `-0.4252` n `239`; crypto_major avg `-0.6416` n `8`; equity avg `-0.2372` n `158`; fx avg `-0.0033` n `6`; index avg `-0.0333` n `27`; metal avg `-0.0534` n `20`; unknown avg `-0.0397` n `1252`
- 4h: commodity avg `0.2557` n `13`; crypto_alt avg `-0.1948` n `239`; crypto_major avg `-1.1373` n `8`; equity avg `0.7201` n `158`; fx avg `-0.0717` n `6`; index avg `0.0822` n `27`; metal avg `0.3912` n `20`; unknown avg `2.1103` n `1236`
- 24h: commodity avg `0.146` n `13`; crypto_alt avg `-2.0116` n `239`; crypto_major avg `-2.5591` n `8`; equity avg `0.5037` n `158`; fx avg `-0.0735` n `6`; index avg `0.0457` n `27`; metal avg `0.4711` n `20`; unknown avg `1.7459` n `990`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
