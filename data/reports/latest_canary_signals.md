# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T11:39:28.266726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0458` n `12`; crypto_alt avg `0.1688` n `229`; crypto_major avg `0.0594` n `8`; equity avg `0.0154` n `91`; fx avg `-0.0103` n `6`; index avg `0.0133` n `25`; metal avg `-0.0872` n `20`; unknown avg `-0.0051` n `763`
- 1h: commodity avg `0.1165` n `12`; crypto_alt avg `0.2792` n `229`; crypto_major avg `-0.0232` n `8`; equity avg `-0.0866` n `91`; fx avg `0.021` n `6`; index avg `0.0059` n `25`; metal avg `-0.1533` n `20`; unknown avg `-0.0429` n `763`
- 4h: commodity avg `0.6027` n `12`; crypto_alt avg `-0.8545` n `229`; crypto_major avg `-0.7421` n `8`; equity avg `-1.5939` n `91`; fx avg `0.0298` n `6`; index avg `-0.3164` n `25`; metal avg `-1.1443` n `20`; unknown avg `-0.1196` n `763`
- 24h: commodity avg `1.3588` n `12`; crypto_alt avg `-3.6258` n `229`; crypto_major avg `-2.9136` n `8`; equity avg `-2.7676` n `91`; fx avg `-0.099` n `6`; index avg `-0.5798` n `25`; metal avg `-1.4674` n `20`; unknown avg `-0.8674` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
