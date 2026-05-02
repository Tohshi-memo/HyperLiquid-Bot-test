# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T11:45:39.886917+00:00`
- Correlation status: `ready`
- Asset price records: `70`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0211` n `7`; crypto_alt avg `-0.1326` n `223`; crypto_major avg `-0.2066` n `7`; equity avg `0.0159` n `42`; fx avg `-0.0029` n `4`; index avg `-0.0002` n `9`; metal avg `-0.0006` n `7`; unknown avg `-0.0766` n `313`
- 1h: commodity avg `0.014` n `7`; crypto_alt avg `-0.2528` n `223`; crypto_major avg `-0.1943` n `7`; equity avg `0.0268` n `42`; fx avg `-0.0173` n `4`; index avg `0.0133` n `9`; metal avg `0.0013` n `7`; unknown avg `-0.0184` n `313`
- 4h: commodity avg `0.0134` n `7`; crypto_alt avg `0.0527` n `223`; crypto_major avg `-0.1365` n `7`; equity avg `0.0017` n `42`; fx avg `0.0123` n `4`; index avg `-0.0085` n `9`; metal avg `0.0327` n `7`; unknown avg `0.0038` n `313`
- 24h: crypto_alt avg `0.6274` n `223`; crypto_major avg `0.4558` n `7`; metal avg `0.7687` n `1`; unknown avg `1.326` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5735`, n `66`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5547`, n `62`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5537`, n `66`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5428`, n `62`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4813`, n `66`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4761`, n `62`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4728`, n `62`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4626`, n `62`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4475`, n `66`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4393`, n `66`, moderate_sample_signal
