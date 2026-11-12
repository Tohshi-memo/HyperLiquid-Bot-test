# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T20:52:30.165928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `13`; crypto_alt avg `0.2267` n `239`; crypto_major avg `0.2384` n `8`; equity avg `0.2389` n `162`; fx avg `0.0051` n `6`; index avg `0.0217` n `27`; metal avg `-0.0042` n `20`; unknown avg `0.3013` n `1261`
- 1h: commodity avg `-0.0279` n `13`; crypto_alt avg `0.1334` n `239`; crypto_major avg `0.0423` n `8`; equity avg `-0.1905` n `162`; fx avg `0.0162` n `6`; index avg `-0.0079` n `27`; metal avg `-0.0477` n `20`; unknown avg `1.0254` n `1241`
- 4h: commodity avg `0.503` n `13`; crypto_alt avg `0.6663` n `239`; crypto_major avg `0.3666` n `8`; equity avg `-0.7019` n `162`; fx avg `0.029` n `6`; index avg `-0.0702` n `27`; metal avg `-0.075` n `20`; unknown avg `46.7067` n `1239`
- 24h: commodity avg `0.8838` n `13`; crypto_alt avg `-2.5095` n `239`; crypto_major avg `-3.1231` n `8`; equity avg `-2.4685` n `162`; fx avg `-0.1239` n `6`; index avg `-0.1412` n `27`; metal avg `-0.7457` n `20`; unknown avg `30.942` n `1135`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
