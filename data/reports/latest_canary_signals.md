# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T05:22:27.955231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0482` n `12`; crypto_alt avg `0.126` n `231`; crypto_major avg `0.1771` n `8`; equity avg `-0.1155` n `122`; fx avg `-0.0057` n `6`; index avg `-0.0265` n `25`; metal avg `0.0119` n `20`; unknown avg `-0.1561` n `797`
- 1h: commodity avg `0.0872` n `12`; crypto_alt avg `-0.4048` n `231`; crypto_major avg `-0.335` n `8`; equity avg `-0.2599` n `122`; fx avg `0.0054` n `6`; index avg `-0.0461` n `25`; metal avg `-0.0002` n `20`; unknown avg `6.9833` n `797`
- 4h: commodity avg `0.0691` n `12`; crypto_alt avg `0.0246` n `231`; crypto_major avg `-0.0352` n `8`; equity avg `0.4207` n `122`; fx avg `-0.0427` n `6`; index avg `0.1225` n `25`; metal avg `0.0588` n `20`; unknown avg `7.6099` n `796`
- 24h: commodity avg `-0.6774` n `12`; crypto_alt avg `-3.2885` n `231`; crypto_major avg `-3.1177` n `8`; equity avg `0.7721` n `122`; fx avg `0.0064` n `6`; index avg `0.1124` n `25`; metal avg `0.1918` n `20`; unknown avg `0.1313` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
