# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T14:52:34.271095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2476` n `13`; crypto_alt avg `0.6085` n `239`; crypto_major avg `0.4985` n `8`; equity avg `1.1267` n `158`; fx avg `-0.0146` n `6`; index avg `0.0839` n `27`; metal avg `0.0974` n `20`; unknown avg `0.8188` n `1257`
- 1h: commodity avg `-0.0486` n `13`; crypto_alt avg `0.9141` n `239`; crypto_major avg `0.4147` n `8`; equity avg `0.2594` n `158`; fx avg `0.0343` n `6`; index avg `0.0498` n `27`; metal avg `0.0695` n `20`; unknown avg `114.26` n `1255`
- 4h: commodity avg `-0.1449` n `13`; crypto_alt avg `1.1268` n `239`; crypto_major avg `0.3944` n `8`; equity avg `0.7838` n `158`; fx avg `0.0312` n `6`; index avg `0.115` n `27`; metal avg `0.0396` n `20`; unknown avg `305.9758` n `1179`
- 24h: commodity avg `0.3779` n `13`; crypto_alt avg `-0.0184` n `239`; crypto_major avg `-2.7688` n `8`; equity avg `0.2517` n `158`; fx avg `-0.0374` n `6`; index avg `-0.1583` n `27`; metal avg `-0.3234` n `20`; unknown avg `57.3813` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
