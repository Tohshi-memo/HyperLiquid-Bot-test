# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T07:07:34.367996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0351` n `13`; crypto_alt avg `-0.1403` n `239`; crypto_major avg `0.153` n `8`; equity avg `-0.1248` n `168`; fx avg `-0.0035` n `6`; index avg `-0.0078` n `27`; metal avg `0.0796` n `20`; unknown avg `0.3095` n `1255`
- 1h: commodity avg `-0.2787` n `13`; crypto_alt avg `0.4298` n `239`; crypto_major avg `0.5328` n `8`; equity avg `-0.071` n `168`; fx avg `-0.024` n `6`; index avg `-0.014` n `27`; metal avg `0.1053` n `20`; unknown avg `0.3611` n `1253`
- 4h: commodity avg `-0.164` n `13`; crypto_alt avg `1.1224` n `239`; crypto_major avg `0.3791` n `8`; equity avg `-0.4881` n `168`; fx avg `-0.0474` n `6`; index avg `-0.0229` n `27`; metal avg `-0.2275` n `20`; unknown avg `26.1206` n `1213`
- 24h: commodity avg `0.2991` n `13`; crypto_alt avg `-2.9186` n `239`; crypto_major avg `-2.8545` n `8`; equity avg `-5.822` n `167`; fx avg `0.1045` n `6`; index avg `-0.5747` n `27`; metal avg `-1.0159` n `20`; unknown avg `695.491` n `1027`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
