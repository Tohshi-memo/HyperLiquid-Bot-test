# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T01:37:27.790697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `0.3086` n `230`; crypto_major avg `0.3402` n `8`; equity avg `-0.2914` n `98`; fx avg `-0.0203` n `6`; index avg `-0.0256` n `25`; metal avg `-0.0788` n `20`; unknown avg `0.0018` n `769`
- 1h: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.1448` n `230`; crypto_major avg `-0.0483` n `8`; equity avg `-0.7253` n `98`; fx avg `-0.0395` n `6`; index avg `-0.1176` n `25`; metal avg `-0.0331` n `20`; unknown avg `0.0321` n `769`
- 4h: commodity avg `-0.0606` n `12`; crypto_alt avg `0.5856` n `230`; crypto_major avg `0.5539` n `8`; equity avg `-0.0318` n `98`; fx avg `-0.0912` n `6`; index avg `0.0675` n `25`; metal avg `0.0046` n `20`; unknown avg `0.179` n `767`
- 24h: commodity avg `-0.1161` n `12`; crypto_alt avg `0.4241` n `230`; crypto_major avg `0.6087` n `8`; equity avg `0.2812` n `97`; fx avg `0.0013` n `6`; index avg `0.0693` n `25`; metal avg `-0.0293` n `20`; unknown avg `0.1689` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1455`, n `670`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `670`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1206`, n `670`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1009`, n `670`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.079`, n `670`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
