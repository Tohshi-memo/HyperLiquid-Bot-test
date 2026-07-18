# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T03:07:30.147529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.0309` n `230`; crypto_major avg `0.0343` n `8`; equity avg `-0.0182` n `96`; fx avg `0.0001` n `6`; index avg `0.0099` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.0625` n `769`
- 1h: commodity avg `-0.0012` n `12`; crypto_alt avg `0.1594` n `230`; crypto_major avg `0.1188` n `8`; equity avg `0.0533` n `96`; fx avg `-0.0093` n `6`; index avg `0.01` n `25`; metal avg `-0.009` n `20`; unknown avg `-0.1163` n `769`
- 4h: commodity avg `-0.0316` n `12`; crypto_alt avg `0.0947` n `230`; crypto_major avg `0.2099` n `8`; equity avg `0.181` n `96`; fx avg `-0.0058` n `6`; index avg `0.0499` n `25`; metal avg `0.0309` n `20`; unknown avg `-0.331` n `769`
- 24h: commodity avg `0.7541` n `12`; crypto_alt avg `-0.3109` n `230`; crypto_major avg `-0.226` n `8`; equity avg `0.5465` n `94`; fx avg `0.0381` n `6`; index avg `0.01` n `25`; metal avg `0.1522` n `20`; unknown avg `0.2416` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
