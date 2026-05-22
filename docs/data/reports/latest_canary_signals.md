# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T13:07:22.664647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0876` n `12`; crypto_alt avg `0.122` n `228`; crypto_major avg `-0.0162` n `8`; equity avg `0.0115` n `67`; fx avg `-0.0134` n `6`; index avg `0.0257` n `23`; metal avg `0.1881` n `18`; unknown avg `0.0013` n `386`
- 1h: commodity avg `-0.4432` n `12`; crypto_alt avg `0.5383` n `228`; crypto_major avg `0.3235` n `8`; equity avg `0.2934` n `67`; fx avg `-0.0178` n `6`; index avg `0.1684` n `23`; metal avg `-0.1544` n `18`; unknown avg `0.4924` n `386`
- 4h: commodity avg `-1.0598` n `12`; crypto_alt avg `0.9263` n `228`; crypto_major avg `0.726` n `8`; equity avg `0.3228` n `67`; fx avg `-0.0587` n `6`; index avg `0.0642` n `23`; metal avg `0.2024` n `18`; unknown avg `0.5755` n `386`
- 24h: commodity avg `-1.9084` n `12`; crypto_alt avg `3.0824` n `228`; crypto_major avg `1.479` n `8`; equity avg `1.4858` n `67`; fx avg `0.0768` n `6`; index avg `1.0165` n `23`; metal avg `0.7276` n `18`; unknown avg `1.6449` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0427`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0416`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0402`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0401`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0372`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.036`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0357`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0347`, n `668`, weak_sample_signal
