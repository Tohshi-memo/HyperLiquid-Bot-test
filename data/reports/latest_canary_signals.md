# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T05:52:26.033012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0227` n `13`; crypto_alt avg `0.1391` n `238`; crypto_major avg `0.0381` n `8`; equity avg `0.0534` n `156`; fx avg `0.0036` n `6`; index avg `0.0055` n `27`; metal avg `-0.0011` n `20`; unknown avg `0.9462` n `1262`
- 1h: commodity avg `0.0132` n `13`; crypto_alt avg `0.1026` n `238`; crypto_major avg `0.0217` n `8`; equity avg `0.0189` n `156`; fx avg `0.0009` n `6`; index avg `0.0049` n `27`; metal avg `-0.0046` n `20`; unknown avg `81.6275` n `1256`
- 4h: commodity avg `0.0649` n `13`; crypto_alt avg `0.4576` n `238`; crypto_major avg `0.078` n `8`; equity avg `0.2075` n `156`; fx avg `-0.0032` n `6`; index avg `0.0353` n `27`; metal avg `-0.0082` n `20`; unknown avg `0.0721` n `1240`
- 24h: commodity avg `0.0011` n `13`; crypto_alt avg `0.8435` n `238`; crypto_major avg `0.3686` n `8`; equity avg `0.2881` n `156`; fx avg `-0.0002` n `6`; index avg `-0.0001` n `27`; metal avg `0.049` n `20`; unknown avg `2.0176` n `996`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
