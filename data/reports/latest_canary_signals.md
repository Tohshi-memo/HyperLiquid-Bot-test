# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T00:52:33.101797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0412` n `12`; crypto_alt avg `-0.0459` n `230`; crypto_major avg `-0.0339` n `8`; equity avg `0.0271` n `96`; fx avg `0.0007` n `6`; index avg `0.0094` n `25`; metal avg `0.0047` n `20`; unknown avg `0.0016` n `769`
- 1h: commodity avg `-0.0344` n `12`; crypto_alt avg `-0.0303` n `230`; crypto_major avg `-0.0085` n `8`; equity avg `0.0935` n `96`; fx avg `0.0011` n `6`; index avg `0.0299` n `25`; metal avg `0.0474` n `20`; unknown avg `-0.1018` n `769`
- 4h: commodity avg `0.0425` n `12`; crypto_alt avg `0.2066` n `230`; crypto_major avg `0.0037` n `8`; equity avg `0.0523` n `96`; fx avg `-0.0217` n `6`; index avg `0.0157` n `25`; metal avg `0.0729` n `20`; unknown avg `-0.1026` n `769`
- 24h: commodity avg `0.6466` n `12`; crypto_alt avg `-0.535` n `230`; crypto_major avg `-0.6306` n `8`; equity avg `-0.4084` n `94`; fx avg `0.0699` n `6`; index avg `-0.1689` n `25`; metal avg `0.058` n `20`; unknown avg `0.1451` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
