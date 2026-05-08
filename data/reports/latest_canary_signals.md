# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T11:37:17.557022+00:00`
- Correlation status: `ready`
- Asset price records: `642`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0428` n `12`; crypto_alt avg `0.0776` n `228`; crypto_major avg `0.0161` n `8`; equity avg `0.058` n `65`; fx avg `0.0186` n `5`; index avg `-0.0085` n `23`; metal avg `0.0819` n `18`; unknown avg `0.0557` n `375`
- 1h: commodity avg `0.06` n `12`; crypto_alt avg `0.1771` n `228`; crypto_major avg `0.1077` n `8`; equity avg `-0.0364` n `65`; fx avg `-0.0153` n `5`; index avg `0.0523` n `23`; metal avg `-0.0477` n `18`; unknown avg `-0.0117` n `375`
- 4h: commodity avg `0.0678` n `12`; crypto_alt avg `0.868` n `228`; crypto_major avg `0.6031` n `8`; equity avg `0.5305` n `65`; fx avg `0.0327` n `5`; index avg `0.1664` n `23`; metal avg `0.3912` n `18`; unknown avg `0.7876` n `375`
- 24h: commodity avg `1.6373` n `12`; crypto_alt avg `1.186` n `228`; crypto_major avg `-1.2588` n `8`; equity avg `-0.5639` n `65`; fx avg `0.2591` n `5`; index avg `-0.391` n `23`; metal avg `-0.4683` n `18`; unknown avg `-0.0965` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1336`, n `634`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1334`, n `634`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `638`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `638`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `638`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `634`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `638`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0799`, n `634`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0791`, n `634`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0773`, n `638`, weak_sample_signal
