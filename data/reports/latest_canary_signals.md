# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T01:22:23.549262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `0.0685` n `230`; crypto_major avg `0.0348` n `8`; equity avg `-0.079` n `96`; fx avg `0.0053` n `6`; index avg `-0.0124` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.105` n `770`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `-0.0537` n `230`; crypto_major avg `0.0582` n `8`; equity avg `0.0788` n `96`; fx avg `0.0407` n `6`; index avg `-0.0087` n `25`; metal avg `0.0054` n `20`; unknown avg `-0.3711` n `770`
- 4h: commodity avg `0.0009` n `12`; crypto_alt avg `0.0373` n `230`; crypto_major avg `0.0852` n `8`; equity avg `0.077` n `96`; fx avg `0.0409` n `6`; index avg `-0.016` n `25`; metal avg `0.0184` n `20`; unknown avg `-0.5661` n `770`
- 24h: commodity avg `0.3659` n `12`; crypto_alt avg `-0.2163` n `230`; crypto_major avg `0.6989` n `8`; equity avg `-0.305` n `96`; fx avg `-0.0563` n `6`; index avg `0.0091` n `25`; metal avg `-0.063` n `20`; unknown avg `0.0264` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
