# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T06:22:18.557651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0097` n `12`; crypto_alt avg `0.072` n `228`; crypto_major avg `-0.1136` n `8`; equity avg `-0.0157` n `67`; fx avg `0.0016` n `6`; index avg `0.0067` n `23`; metal avg `0.0151` n `18`; unknown avg `-0.0276` n `386`
- 1h: commodity avg `-0.0505` n `12`; crypto_alt avg `0.1392` n `228`; crypto_major avg `-0.0125` n `8`; equity avg `0.0136` n `67`; fx avg `0.0026` n `6`; index avg `-0.0058` n `23`; metal avg `0.0228` n `18`; unknown avg `0.9504` n `376`
- 4h: commodity avg `-0.0539` n `12`; crypto_alt avg `-0.3131` n `228`; crypto_major avg `-0.0358` n `8`; equity avg `-0.0455` n `67`; fx avg `0.0078` n `6`; index avg `-0.0422` n `23`; metal avg `0.0257` n `18`; unknown avg `0.6333` n `376`
- 24h: commodity avg `-0.1517` n `12`; crypto_alt avg `-3.9212` n `228`; crypto_major avg `-2.6786` n `8`; equity avg `-1.9522` n `67`; fx avg `0.0351` n `6`; index avg `-0.1853` n `23`; metal avg `-0.7983` n `18`; unknown avg `-1.2146` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
