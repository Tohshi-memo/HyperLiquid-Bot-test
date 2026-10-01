# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T14:22:36.462863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `13`; crypto_alt avg `-0.0535` n `234`; crypto_major avg `-0.0333` n `8`; equity avg `-0.0732` n `142`; fx avg `-0.0222` n `6`; index avg `-0.0338` n `26`; metal avg `-0.0602` n `20`; unknown avg `0.3299` n `975`
- 1h: commodity avg `0.1209` n `13`; crypto_alt avg `-0.2124` n `234`; crypto_major avg `0.1354` n `8`; equity avg `-0.7524` n `142`; fx avg `-0.0134` n `6`; index avg `-0.2027` n `26`; metal avg `-0.1866` n `20`; unknown avg `119.7611` n `973`
- 4h: commodity avg `0.0395` n `13`; crypto_alt avg `-0.4735` n `234`; crypto_major avg `0.0917` n `8`; equity avg `-0.94` n `142`; fx avg `-0.039` n `6`; index avg `-0.2185` n `26`; metal avg `-0.0645` n `20`; unknown avg `1.8165` n `967`
- 24h: commodity avg `-0.1739` n `13`; crypto_alt avg `-1.3904` n `234`; crypto_major avg `0.0935` n `8`; equity avg `-0.7943` n `142`; fx avg `0.0509` n `6`; index avg `-0.2232` n `26`; metal avg `-0.2898` n `20`; unknown avg `2.9134` n `786`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
