# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T21:52:18.607221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2199` n `12`; crypto_alt avg `-0.0088` n `228`; crypto_major avg `0.0408` n `8`; equity avg `-0.0263` n `66`; fx avg `-0.0006` n `6`; index avg `0.0194` n `23`; metal avg `0.018` n `18`; unknown avg `-0.0181` n `384`
- 1h: commodity avg `0.1947` n `12`; crypto_alt avg `-0.1122` n `228`; crypto_major avg `0.1853` n `8`; equity avg `-0.0505` n `66`; fx avg `-0.0044` n `6`; index avg `0.0512` n `23`; metal avg `-0.0009` n `18`; unknown avg `-0.0439` n `384`
- 4h: commodity avg `0.6845` n `12`; crypto_alt avg `-0.0247` n `228`; crypto_major avg `0.0223` n `8`; equity avg `0.0273` n `66`; fx avg `-0.0482` n `6`; index avg `0.162` n `23`; metal avg `0.0183` n `18`; unknown avg `-0.1684` n `384`
- 24h: commodity avg `-2.066` n `12`; crypto_alt avg `2.6222` n `228`; crypto_major avg `2.044` n `8`; equity avg `1.5562` n `66`; fx avg `-0.0856` n `6`; index avg `1.1251` n `23`; metal avg `1.4908` n `18`; unknown avg `0.9972` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
