# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T03:37:28.358712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `0.1587` n `229`; crypto_major avg `0.1875` n `8`; equity avg `0.2482` n `91`; fx avg `-0.0076` n `6`; index avg `0.1006` n `25`; metal avg `0.0654` n `20`; unknown avg `-0.028` n `764`
- 1h: commodity avg `-0.0389` n `12`; crypto_alt avg `-0.0314` n `229`; crypto_major avg `0.0883` n `8`; equity avg `-0.254` n `91`; fx avg `0.0014` n `6`; index avg `-0.0237` n `25`; metal avg `-0.1277` n `20`; unknown avg `-0.2596` n `764`
- 4h: commodity avg `-0.0295` n `12`; crypto_alt avg `0.0271` n `229`; crypto_major avg `-0.1411` n `8`; equity avg `-0.1122` n `91`; fx avg `0.013` n `6`; index avg `-0.1044` n `25`; metal avg `-0.1155` n `20`; unknown avg `-0.4267` n `764`
- 24h: commodity avg `0.2979` n `12`; crypto_alt avg `-0.6096` n `229`; crypto_major avg `-1.0934` n `8`; equity avg `0.1168` n `91`; fx avg `0.0314` n `6`; index avg `-0.2079` n `25`; metal avg `-1.1088` n `20`; unknown avg `-0.0405` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
