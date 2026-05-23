# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T05:37:17.591415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.054` n `12`; crypto_alt avg `0.0592` n `228`; crypto_major avg `0.0936` n `8`; equity avg `0.013` n `67`; fx avg `0.0037` n `6`; index avg `0.0037` n `23`; metal avg `0.0013` n `18`; unknown avg `0.0403` n `386`
- 1h: commodity avg `-0.0586` n `12`; crypto_alt avg `-0.3792` n `228`; crypto_major avg `-0.1463` n `8`; equity avg `-0.1064` n `67`; fx avg `0.0098` n `6`; index avg `-0.0893` n `23`; metal avg `-0.0392` n `18`; unknown avg `-0.3531` n `386`
- 4h: commodity avg `-0.0563` n `12`; crypto_alt avg `-0.3394` n `228`; crypto_major avg `-0.1337` n `8`; equity avg `-0.0305` n `67`; fx avg `0.0066` n `6`; index avg `-0.0121` n `23`; metal avg `0.0176` n `18`; unknown avg `-0.7626` n `386`
- 24h: commodity avg `-0.0028` n `12`; crypto_alt avg `-4.124` n `228`; crypto_major avg `-2.7016` n `8`; equity avg `-2.064` n `67`; fx avg `0.0421` n `6`; index avg `-0.1761` n `23`; metal avg `-1.154` n `18`; unknown avg `-2.2825` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
