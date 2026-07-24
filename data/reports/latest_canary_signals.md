# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T19:22:26.729363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.0554` n `230`; crypto_major avg `0.1026` n `8`; equity avg `-0.0197` n `100`; fx avg `0.0055` n `6`; index avg `-0.0148` n `25`; metal avg `-0.0201` n `20`; unknown avg `0.0283` n `773`
- 1h: commodity avg `0.0726` n `12`; crypto_alt avg `-0.0456` n `230`; crypto_major avg `0.0656` n `8`; equity avg `-0.5722` n `100`; fx avg `0.008` n `6`; index avg `-0.1153` n `25`; metal avg `-0.0702` n `20`; unknown avg `-0.1017` n `773`
- 4h: commodity avg `0.0392` n `12`; crypto_alt avg `0.0139` n `230`; crypto_major avg `-0.0317` n `8`; equity avg `-1.2946` n `100`; fx avg `-0.0169` n `6`; index avg `-0.26` n `25`; metal avg `-0.2287` n `20`; unknown avg `-0.191` n `773`
- 24h: commodity avg `-0.4422` n `12`; crypto_alt avg `-0.8593` n `230`; crypto_major avg `-0.6689` n `8`; equity avg `-3.0452` n `100`; fx avg `-0.1526` n `6`; index avg `-0.406` n `25`; metal avg `-0.0028` n `20`; unknown avg `14.0666` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1285`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1237`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1159`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1112`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `666`, weak_sample_signal
