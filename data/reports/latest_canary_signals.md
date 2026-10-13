# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T14:22:26.455754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1661` n `13`; crypto_alt avg `0.206` n `235`; crypto_major avg `0.1558` n `8`; equity avg `0.0607` n `151`; fx avg `-0.009` n `6`; index avg `-0.0208` n `26`; metal avg `-0.0476` n `20`; unknown avg `0.2757` n `1119`
- 1h: commodity avg `0.2712` n `13`; crypto_alt avg `0.3468` n `235`; crypto_major avg `0.5041` n `8`; equity avg `0.6538` n `151`; fx avg `-0.0035` n `6`; index avg `0.0506` n `26`; metal avg `-0.1439` n `20`; unknown avg `1.8782` n `1113`
- 4h: commodity avg `0.7024` n `13`; crypto_alt avg `0.2387` n `235`; crypto_major avg `0.3303` n `8`; equity avg `-0.2448` n `151`; fx avg `0.066` n `6`; index avg `-0.0493` n `26`; metal avg `-0.284` n `20`; unknown avg `1.8201` n `1103`
- 24h: commodity avg `0.2487` n `13`; crypto_alt avg `-2.3022` n `235`; crypto_major avg `-0.9145` n `8`; equity avg `-1.4841` n `151`; fx avg `0.1029` n `6`; index avg `-0.2275` n `26`; metal avg `-0.1737` n `20`; unknown avg `-0.2159` n `994`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1627`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1466`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1416`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0851`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
