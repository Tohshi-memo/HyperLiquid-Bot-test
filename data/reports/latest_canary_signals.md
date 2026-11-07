# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T11:07:25.874954+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `13`; crypto_alt avg `0.0696` n `239`; crypto_major avg `0.1237` n `8`; equity avg `-0.001` n `158`; fx avg `0.0081` n `6`; index avg `0.0025` n `27`; metal avg `0.0081` n `20`; unknown avg `-0.034` n `1257`
- 1h: commodity avg `0.02` n `13`; crypto_alt avg `-0.1622` n `239`; crypto_major avg `-0.0373` n `8`; equity avg `-0.0245` n `158`; fx avg `0.0016` n `6`; index avg `0.0082` n `27`; metal avg `0.0124` n `20`; unknown avg `-0.0766` n `1255`
- 4h: commodity avg `0.0532` n `13`; crypto_alt avg `-0.6438` n `239`; crypto_major avg `-0.0913` n `8`; equity avg `0.0834` n `158`; fx avg `-0.0049` n `6`; index avg `0.0077` n `27`; metal avg `0.011` n `20`; unknown avg `101.8674` n `1197`
- 24h: commodity avg `-0.0698` n `13`; crypto_alt avg `-1.097` n `239`; crypto_major avg `-0.2492` n `8`; equity avg `0.0083` n `158`; fx avg `0.0049` n `6`; index avg `0.0356` n `27`; metal avg `0.1344` n `20`; unknown avg `7.6211` n `1059`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
