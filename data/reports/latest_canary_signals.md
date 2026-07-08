# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T03:22:27.437012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.5508` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.6293` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5122` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `0.1425` n `229`; crypto_major avg `0.1209` n `8`; equity avg `0.19` n `91`; fx avg `0.0043` n `6`; index avg `0.0353` n `25`; metal avg `0.0554` n `20`; unknown avg `0.4852` n `763`
- 1h: commodity avg `-0.0201` n `12`; crypto_alt avg `0.5888` n `229`; crypto_major avg `0.5338` n `8`; equity avg `0.3803` n `91`; fx avg `-0.041` n `6`; index avg `0.0852` n `25`; metal avg `0.1682` n `20`; unknown avg `1.0522` n `763`
- 4h: commodity avg `-0.013` n `12`; crypto_alt avg `-0.9802` n `229`; crypto_major avg `-1.3656` n `8`; equity avg `1.1852` n `91`; fx avg `-0.0366` n `6`; index avg `0.1466` n `25`; metal avg `0.2637` n `20`; unknown avg `1.2633` n `763`
- 24h: commodity avg `0.8947` n `12`; crypto_alt avg `-2.3341` n `229`; crypto_major avg `-1.6851` n `8`; equity avg `-1.0821` n `91`; fx avg `-0.1674` n `6`; index avg `-0.1229` n `25`; metal avg `-0.0683` n `20`; unknown avg `-0.3106` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
