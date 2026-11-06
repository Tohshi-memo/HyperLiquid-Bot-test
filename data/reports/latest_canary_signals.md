# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T18:52:29.113625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `13`; crypto_alt avg `-0.1216` n `239`; crypto_major avg `-0.0312` n `8`; equity avg `0.167` n `158`; fx avg `0.0077` n `6`; index avg `0.0251` n `27`; metal avg `0.0639` n `20`; unknown avg `2.5371` n `1261`
- 1h: commodity avg `0.1158` n `13`; crypto_alt avg `0.2316` n `239`; crypto_major avg `0.3802` n `8`; equity avg `0.9779` n `158`; fx avg `0.0255` n `6`; index avg `0.108` n `27`; metal avg `0.165` n `20`; unknown avg `14.3268` n `1253`
- 4h: commodity avg `0.0486` n `13`; crypto_alt avg `-0.5001` n `239`; crypto_major avg `0.0776` n `8`; equity avg `-0.7698` n `158`; fx avg `-0.0076` n `6`; index avg `-0.0718` n `27`; metal avg `0.0981` n `20`; unknown avg `14.3532` n `1245`
- 24h: commodity avg `0.2002` n `13`; crypto_alt avg `1.6995` n `239`; crypto_major avg `-0.2395` n `8`; equity avg `2.2868` n `158`; fx avg `-0.0934` n `6`; index avg `0.2186` n `27`; metal avg `-0.0943` n `20`; unknown avg `44.0956` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
