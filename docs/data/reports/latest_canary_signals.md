# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T00:52:14.312940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1424` n `12`; crypto_alt avg `-0.0285` n `228`; crypto_major avg `-0.0451` n `8`; equity avg `-0.0072` n `67`; fx avg `-0.0213` n `6`; index avg `0.0546` n `23`; metal avg `-0.0208` n `18`; unknown avg `-0.07` n `396`
- 1h: commodity avg `-0.0747` n `12`; crypto_alt avg `0.2092` n `228`; crypto_major avg `-0.1313` n `8`; equity avg `0.0751` n `67`; fx avg `-0.0866` n `6`; index avg `0.1347` n `23`; metal avg `-0.0471` n `18`; unknown avg `0.0251` n `396`
- 4h: commodity avg `-0.9383` n `12`; crypto_alt avg `0.4941` n `228`; crypto_major avg `0.5037` n `8`; equity avg `0.0669` n `67`; fx avg `-0.0989` n `6`; index avg `0.121` n `23`; metal avg `1.4044` n `18`; unknown avg `0.2507` n `396`
- 24h: commodity avg `0.2264` n `12`; crypto_alt avg `-1.3244` n `228`; crypto_major avg `0.335` n `8`; equity avg `0.3204` n `67`; fx avg `-0.032` n `6`; index avg `-0.1006` n `23`; metal avg `0.9515` n `18`; unknown avg `-0.2707` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
