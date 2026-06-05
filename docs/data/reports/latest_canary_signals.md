# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T00:37:21.453447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1209` n `12`; crypto_alt avg `0.2247` n `228`; crypto_major avg `0.2847` n `8`; equity avg `0.0976` n `74`; fx avg `0.0066` n `6`; index avg `-0.0211` n `23`; metal avg `0.1587` n `18`; unknown avg `0.0794` n `424`
- 1h: commodity avg `-0.0908` n `12`; crypto_alt avg `0.1954` n `228`; crypto_major avg `0.0812` n `8`; equity avg `-0.6275` n `74`; fx avg `0.0621` n `6`; index avg `-0.4919` n `23`; metal avg `-0.2318` n `18`; unknown avg `1.0009` n `424`
- 4h: commodity avg `-0.1244` n `12`; crypto_alt avg `-1.261` n `228`; crypto_major avg `-0.6418` n `8`; equity avg `-1.1598` n `74`; fx avg `0.0717` n `6`; index avg `-0.7027` n `23`; metal avg `-0.3856` n `18`; unknown avg `0.0517` n `424`
- 24h: commodity avg `-0.5676` n `12`; crypto_alt avg `-5.2798` n `228`; crypto_major avg `-2.7852` n `8`; equity avg `-1.4825` n `73`; fx avg `0.1355` n `6`; index avg `-0.4755` n `23`; metal avg `0.3306` n `18`; unknown avg `-0.2222` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
