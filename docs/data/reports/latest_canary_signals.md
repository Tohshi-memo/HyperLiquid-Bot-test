# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T01:52:19.250660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `12`; crypto_alt avg `-0.1107` n `228`; crypto_major avg `-0.1631` n `8`; equity avg `0.0811` n `67`; fx avg `0.0` n `6`; index avg `0.0135` n `23`; metal avg `0.0237` n `18`; unknown avg `-0.184` n `386`
- 1h: commodity avg `0.1147` n `12`; crypto_alt avg `0.4804` n `228`; crypto_major avg `0.0953` n `8`; equity avg `0.1776` n `67`; fx avg `-0.0007` n `6`; index avg `0.0774` n `23`; metal avg `0.0192` n `18`; unknown avg `-0.583` n `386`
- 4h: commodity avg `0.6712` n `12`; crypto_alt avg `-1.1738` n `228`; crypto_major avg `-1.0483` n `8`; equity avg `-0.4772` n `67`; fx avg `0.0011` n `6`; index avg `-0.1413` n `23`; metal avg `-0.1373` n `18`; unknown avg `-1.1273` n `386`
- 24h: commodity avg `0.0934` n `12`; crypto_alt avg `-3.3317` n `228`; crypto_major avg `-2.6429` n `8`; equity avg `-1.5939` n `67`; fx avg `0.0924` n `6`; index avg `-0.0203` n `23`; metal avg `-0.9275` n `18`; unknown avg `-2.0129` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
