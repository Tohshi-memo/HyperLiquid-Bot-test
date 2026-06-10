# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T15:22:34.160945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0431` n `12`; crypto_alt avg `0.2694` n `228`; crypto_major avg `0.1737` n `8`; equity avg `-0.2628` n `74`; fx avg `-0.0049` n `6`; index avg `-0.2795` n `23`; metal avg `0.0023` n `18`; unknown avg `0.1427` n `548`
- 1h: commodity avg `-0.2346` n `12`; crypto_alt avg `0.2406` n `228`; crypto_major avg `0.1044` n `8`; equity avg `-1.0928` n `74`; fx avg `-0.0006` n `6`; index avg `-0.8929` n `23`; metal avg `-0.56` n `18`; unknown avg `0.0018` n `548`
- 4h: commodity avg `0.0573` n `12`; crypto_alt avg `1.8358` n `228`; crypto_major avg `1.5979` n `8`; equity avg `1.02` n `74`; fx avg `-0.0075` n `6`; index avg `0.1779` n `23`; metal avg `0.1772` n `18`; unknown avg `1.3902` n `547`
- 24h: commodity avg `0.9886` n `12`; crypto_alt avg `0.715` n `228`; crypto_major avg `-0.3601` n `8`; equity avg `-0.7789` n `74`; fx avg `-0.0767` n `6`; index avg `-0.9127` n `23`; metal avg `-1.8447` n `18`; unknown avg `-0.3289` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
