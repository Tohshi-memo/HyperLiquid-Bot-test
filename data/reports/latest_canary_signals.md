# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T02:22:24.250135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.1939` n `231`; crypto_major avg `-0.3309` n `8`; equity avg `0.0336` n `126`; fx avg `-0.0016` n `6`; index avg `0.0011` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.0305` n `793`
- 1h: commodity avg `-0.0981` n `12`; crypto_alt avg `0.123` n `231`; crypto_major avg `0.195` n `8`; equity avg `0.1819` n `126`; fx avg `0.0115` n `6`; index avg `0.0673` n `25`; metal avg `0.0794` n `20`; unknown avg `-0.0708` n `793`
- 4h: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0406` n `231`; crypto_major avg `-0.3644` n `8`; equity avg `-0.3164` n `126`; fx avg `-0.0675` n `6`; index avg `-0.0941` n `25`; metal avg `0.1756` n `20`; unknown avg `1.0204` n `793`
- 24h: commodity avg `0.401` n `12`; crypto_alt avg `0.4774` n `231`; crypto_major avg `0.603` n `8`; equity avg `1.4442` n `126`; fx avg `-0.0873` n `6`; index avg `0.2595` n `25`; metal avg `-0.2135` n `20`; unknown avg `0.7229` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
