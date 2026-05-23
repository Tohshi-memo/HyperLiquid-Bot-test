# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T17:22:15.411220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `0.0745` n `228`; crypto_major avg `-0.0217` n `8`; equity avg `-0.0026` n `67`; fx avg `0.0068` n `6`; index avg `-0.0115` n `23`; metal avg `0.0107` n `18`; unknown avg `0.2122` n `396`
- 1h: commodity avg `0.0525` n `12`; crypto_alt avg `0.4594` n `228`; crypto_major avg `0.1951` n `8`; equity avg `-0.018` n `67`; fx avg `-0.0015` n `6`; index avg `0.0283` n `23`; metal avg `0.0419` n `18`; unknown avg `-0.0259` n `396`
- 4h: commodity avg `-0.7568` n `12`; crypto_alt avg `1.6315` n `228`; crypto_major avg `1.015` n `8`; equity avg `0.5122` n `67`; fx avg `0.0021` n `6`; index avg `0.187` n `23`; metal avg `0.1959` n `18`; unknown avg `0.912` n `396`
- 24h: commodity avg `0.0574` n `12`; crypto_alt avg `-2.5851` n `228`; crypto_major avg `-1.879` n `8`; equity avg `-0.9347` n `67`; fx avg `0.0114` n `6`; index avg `-0.2474` n `23`; metal avg `-0.1715` n `18`; unknown avg `-1.4905` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
