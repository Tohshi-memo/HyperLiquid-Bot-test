# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T08:52:20.878972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1385` n `12`; crypto_alt avg `-0.0191` n `228`; crypto_major avg `0.109` n `8`; equity avg `-0.1478` n `67`; fx avg `-0.0016` n `6`; index avg `0.037` n `23`; metal avg `-0.0357` n `18`; unknown avg `-0.3608` n `386`
- 1h: commodity avg `-0.0541` n `12`; crypto_alt avg `-0.1499` n `228`; crypto_major avg `0.2133` n `8`; equity avg `-0.0989` n `67`; fx avg `0.0236` n `6`; index avg `0.0978` n `23`; metal avg `0.0596` n `18`; unknown avg `-0.3855` n `386`
- 4h: commodity avg `0.5023` n `12`; crypto_alt avg `-0.0217` n `228`; crypto_major avg `0.1083` n `8`; equity avg `-0.1912` n `67`; fx avg `0.0001` n `6`; index avg `0.0771` n `23`; metal avg `-0.4222` n `18`; unknown avg `-0.1279` n `376`
- 24h: commodity avg `-0.2324` n `12`; crypto_alt avg `1.4258` n `228`; crypto_major avg `0.032` n `8`; equity avg `1.2107` n `67`; fx avg `0.1318` n `6`; index avg `0.7949` n `23`; metal avg `0.2807` n `18`; unknown avg `1.05` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0434`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0366`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0362`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0352`, n `668`, weak_sample_signal
