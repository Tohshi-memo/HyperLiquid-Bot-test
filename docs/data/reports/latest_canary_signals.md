# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T21:52:27.496076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `13`; crypto_alt avg `0.3821` n `238`; crypto_major avg `0.2881` n `8`; equity avg `0.2139` n `155`; fx avg `-0.0013` n `6`; index avg `0.0324` n `27`; metal avg `0.01` n `20`; unknown avg `177.9729` n `1238`
- 1h: commodity avg `0.0016` n `13`; crypto_alt avg `0.4878` n `238`; crypto_major avg `0.3569` n `8`; equity avg `0.2332` n `155`; fx avg `-0.0061` n `6`; index avg `0.013` n `27`; metal avg `-0.0067` n `20`; unknown avg `5.5156` n `1224`
- 4h: commodity avg `-0.2422` n `13`; crypto_alt avg `1.6225` n `238`; crypto_major avg `0.8472` n `8`; equity avg `-0.2828` n `155`; fx avg `-0.0133` n `6`; index avg `-0.0767` n `27`; metal avg `0.1288` n `20`; unknown avg `4.5953` n `1114`
- 24h: commodity avg `0.1307` n `13`; crypto_alt avg `1.0306` n `238`; crypto_major avg `0.753` n `8`; equity avg `0.9639` n `154`; fx avg `0.2467` n `6`; index avg `0.1649` n `27`; metal avg `-0.1236` n `20`; unknown avg `24.5625` n `1060`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
