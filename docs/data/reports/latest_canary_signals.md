# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T21:31:37.625832+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.0855` n `230`; crypto_major avg `-0.0318` n `8`; equity avg `0.0034` n `114`; fx avg `-0.0011` n `6`; index avg `-0.0` n `25`; metal avg `-0.0182` n `20`; unknown avg `-0.0895` n `791`
- 1h: commodity avg `-0.0334` n `12`; crypto_alt avg `-0.4576` n `230`; crypto_major avg `-0.1721` n `8`; equity avg `0.0189` n `114`; fx avg `0.0058` n `6`; index avg `-0.01` n `25`; metal avg `-0.0196` n `20`; unknown avg `0.2734` n `791`
- 4h: commodity avg `0.0282` n `12`; crypto_alt avg `-0.5735` n `230`; crypto_major avg `-0.3501` n `8`; equity avg `0.04` n `114`; fx avg `0.0195` n `6`; index avg `0.0045` n `25`; metal avg `-0.0461` n `20`; unknown avg `0.1038` n `791`
- 24h: commodity avg `0.0514` n `12`; crypto_alt avg `-0.7746` n `230`; crypto_major avg `-0.3023` n `8`; equity avg `0.2871` n `114`; fx avg `0.001` n `6`; index avg `0.04` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.0071` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2199`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
